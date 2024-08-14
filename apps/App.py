import argparse
from datetime import datetime
from pytz import timezone

class Order(object):
    
    def __init__(self, order_id: str, customer_name: str, order_date: str, order_time: str, total_amount: float):
        
        self.order_id       = order_id
        self.customer_name  = customer_name
        self.order_date     = order_date if order_date else datetime.now().strftime("%d-%m-%Y")
        
        utc                 = datetime.now(timezone('UTC'))
        time                = utc.astimezone(timezone('Asia/Jakarta'))
        
        self.order_time     = order_time if order_time else time.strftime("%I:%M %p")
        self.total_amount   = total_amount

    def calculate_tax(self, tax_rate: float):
        
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1")
        return self.total_amount * tax_rate

    def display_order(self, tax_rate: float):
        
        tax_amount = self.calculate_tax(tax_rate)
        print(f"\n{'ORDER': ^40}\n{'=' * 40}")
        print(f"Order ID        : {self.order_id}")
        print(f"Customer Name   : {self.customer_name}")
        print(f"Order Date      : {self.order_date}")
        print(f"Order Time      : {self.order_time}") 
        print(f"Total Amount    : Rp.{self.total_amount:.2f}")
        print(f"Tax Amount      : Rp.{tax_amount:.2f}")
        print(f"Tax Rate        : {tax_rate:.2%}")
        print(f"{'=' * 40}")

class OrderProcessor(object):

    def __init__(self):
        
        self.orders = []

    def add_order(self, order: Order):
        
        self.orders.append(order)

    def calculate_total_revenue(self):
        
        return sum(order.total_amount for order in self.orders)

    def calculate_total_tax(self, tax_rate: float):
        
        return sum(order.calculate_tax(tax_rate) for order in self.orders)

    def display_orders(self, tax_rate: float):
        
        for order in self.orders:
            order.display_order(tax_rate)
            print("\n")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Process orders.....")

    parser.add_argument('--order_id', type= str, help="Order ID")
    parser.add_argument('--customer_name', type= str, help="Customer Name")
    parser.add_argument('--order_date', type= datetime, help="Order Date")
    parser.add_argument('--order_time', type= str, help="Order Time (AM/PM) Timezone Asia")
    parser.add_argument('--total_amount', type=float, help="Total Amount")
    parser.add_argument('--tax_rate', type=float, default=0.07, help="Tax rate to apply")

    args = parser.parse_args()

    processor = OrderProcessor()
    
    order = Order(
        order_id=args.order_id,
        customer_name=args.customer_name,
        order_date=args.order_date,
        order_time=args.order_time,
        total_amount=args.total_amount
    )
    
    processor.add_order(order)

    processor.display_orders(args.tax_rate)

    print(f"{'CALCULATION REVENUE AND TAX': ^40}\n{'=' * 40}")
    print(f"Total Revenue   : Rp.{processor.calculate_total_revenue():.2f}")
    print(f"Total Tax       : Rp.{processor.calculate_total_tax(args.tax_rate):.2f}")
    print(f"{'=' * 40}\n{'THANK YOU': ^40}")