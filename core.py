

class SystemEngineManager:

    def __init__(self):
        self.services_list = [
            {"service_name":"Mobile service", "service_code":"*149*01#"}
        ]
        self.services_code = ["*149*01#"]
        self.vouchers_list = []
        self.system_money_balance = 0
        self.company_customers = []

    def start_system(self):
        try:
            service_code = input("Enter service code")
            while service_code:
                if service_code not in self.services_list["service_code"]:
                    print("Invalid ussd")
                    service_code
                else:
                    for service in self.services_list:
                        if service["service_code"] == service_code:
                            print(service)
                break
        except Exception as systemError:
            print(f"An error occured {systemError}")
