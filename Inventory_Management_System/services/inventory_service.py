from models.product import Product
from utils.file_handler import load_data, save_data


class InventoryService:
    """
    Handles all business logic for inventory management.
    Separates data logic from UI logic (Single Responsibility Principle).
    """

    def __init__(self):
        self._products: list[Product] = self._load_products()

    # ---------- Private Helpers ----------

    def _load_products(self) -> list[Product]:
        raw = load_data()
        return [Product.from_dict(item) for item in raw]

    def _save_products(self):
        save_data([p.to_dict() for p in self._products])

    def _next_id(self) -> int:
        if not self._products:
            return 1
        return max(p.id for p in self._products) + 1

    def _find_by_id(self, product_id: int) -> Product | None:
        for p in self._products:
            if p.id == product_id:
                return p
        return None

    # ---------- CRUD Operations ----------

    def add_product(self, name: str, price: float, stock: int) -> Product:
        """Create a new product and save it."""
        product = Product(
            product_id=self._next_id(),
            name=name,
            price=price,
            stock=stock,
        )
        self._products.append(product)
        self._save_products()
        return product

    def get_all_products(self) -> list[Product]:
        """Return all products in the inventory."""
        return list(self._products)

    def get_product_by_id(self, product_id: int) -> Product | None:
        """Find and return a product by its ID."""
        return self._find_by_id(product_id)

    def update_product(self, product_id: int, name: str = None, price: float = None, stock: int = None) -> Product | None:
        """Update product fields. Only provided fields are changed."""
        product = self._find_by_id(product_id)
        if not product:
            return None
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock
        self._save_products()
        return product

    def delete_product(self, product_id: int) -> bool:
        """Remove a product by ID. Returns True if deleted, False if not found."""
        product = self._find_by_id(product_id)
        if not product:
            return False
        self._products.remove(product)
        self._save_products()
        return True

    def search_products(self, keyword: str) -> list[Product]:
        """Search products by name (case-insensitive)."""
        keyword = keyword.lower()
        return [p for p in self._products if keyword in p.name.lower()]
