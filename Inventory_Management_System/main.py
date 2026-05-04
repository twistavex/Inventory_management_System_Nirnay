import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.inventory_service import InventoryService


service = InventoryService()


def display_menu():
    print("\n" + "=" * 40)
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. View All Products")
    print("  2. Add New Product")
    print("  3. Update Product")
    print("  4. Delete Product")
    print("  5. Search Products")
    print("  6. View Product by ID")
    print("  0. Exit")
    print("=" * 40)


def view_all():
    products = service.get_all_products()
    if not products:
        print("\n  No products in inventory.")
        return
    print(f"\n  {'ID':<5} {'Name':<20} {'Price':>10} {'Stock':>8}")
    print("  " + "-" * 45)
    for p in products:
        print(f"  {p.id:<5} {p.name:<20} ₹{p.price:>9.2f} {p.stock:>8}")


def add_product():
    print("\n--- Add New Product ---")
    name = input("  Product name: ").strip()
    price = float(input("  Price (₹): "))
    stock = int(input("  Stock quantity: "))
    product = service.add_product(name, price, stock)
    print(f"\n  ✅ Product added: {product}")


def update_product():
    print("\n--- Update Product ---")
    product_id = int(input("  Enter product ID to update: "))
    product = service.get_product_by_id(product_id)
    if not product:
        print("  ❌ Product not found.")
        return
    print(f"  Current: {product}")
    print("  (Press Enter to keep current value)")
    name = input(f"  New name [{product.name}]: ").strip() or None
    price_input = input(f"  New price [{product.price}]: ").strip()
    price = float(price_input) if price_input else None
    stock_input = input(f"  New stock [{product.stock}]: ").strip()
    stock = int(stock_input) if stock_input else None
    updated = service.update_product(product_id, name=name, price=price, stock=stock)
    print(f"\n  ✅ Updated: {updated}")


def delete_product():
    print("\n--- Delete Product ---")
    product_id = int(input("  Enter product ID to delete: "))
    confirm = input(f"  Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("  Cancelled.")
        return
    success = service.delete_product(product_id)
    if success:
        print("  ✅ Product deleted.")
    else:
        print("  ❌ Product not found.")


def search_products():
    print("\n--- Search Products ---")
    keyword = input("  Enter search keyword: ").strip()
    results = service.search_products(keyword)
    if not results:
        print("  No matching products found.")
    else:
        print(f"\n  Found {len(results)} result(s):")
        for p in results:
            print(f"   {p}")


def view_by_id():
    print("\n--- View Product by ID ---")
    product_id = int(input("  Enter product ID: "))
    product = service.get_product_by_id(product_id)
    if product:
        print(f"\n  {product}")
        print(f"  Full repr: {repr(product)}")
    else:
        print("  ❌ Product not found.")


def main():
    print("\n  Welcome to Inventory Manager!")
    while True:
        display_menu()
        choice = input("  Enter your choice: ").strip()
        try:
            if choice == "1":
                view_all()
            elif choice == "2":
                add_product()
            elif choice == "3":
                update_product()
            elif choice == "4":
                delete_product()
            elif choice == "5":
                search_products()
            elif choice == "6":
                view_by_id()
            elif choice == "0":
                print("\n  Goodbye! 👋\n")
                break
            else:
                print("  ⚠️  Invalid choice. Please try again.")
        except ValueError as e:
            print(f"  ⚠️  Invalid input: {e}")
        except Exception as e:
            print(f"  ❌ Error: {e}")


if __name__ == "__main__":
    main()
