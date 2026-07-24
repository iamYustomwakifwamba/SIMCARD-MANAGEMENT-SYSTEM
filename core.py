from database import get_all_services, get_all_customers, get_admin_users_only

class SystemEngineManager:

    def __init__(self):
        self.services_list = get_all_services()
        self.services_code = ["*149*01#"]
        self.vouchers_list = []
        self.system_money_balance = 0
        self.company_customers = get_all_customers()

    def admin_panel_portal(self):
        self.admin_services = [
            "1.open customers list",
            "1.open vouchers list",
            "3.add new customer"
        ]
        self.admin_accounts = get_admin_users_only()

    def start_system(self):
        try:
            
            service_code = input("Enter service code")
            while service_code:
                if service_code not in (element["service_code"] for element in self.services_list):
                    print("Invalid ussd")
                else:
                    for service in self.services_list:
                        if service["service_code"] == service_code:
                            print(service["service_name"])

                            

                break
        except Exception as systemError:
            print(f"An error occured {systemError}") 
