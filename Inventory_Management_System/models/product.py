class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self._id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    # --- Getters (Encapsulation) ---
    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    # --- Setters with validation (Abstraction) ---
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Product name cannot be empty.")
        self._name = value.strip()

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = round(value, 2)

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    # --- Magic Methods ---
    def __str__(self) -> str:
        return f"[{self._id}] {self._name} | Price: ₹{self._price:.2f} | Stock: {self._stock}"

    def __repr__(self) -> str:
        return f"Product(id={self._id}, name='{self._name}', price={self._price}, stock={self._stock})"

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(
            product_id=data["id"],
            name=data["name"],
            price=data["price"],
            stock=data["stock"],
        )
