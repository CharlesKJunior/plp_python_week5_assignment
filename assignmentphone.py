## assignment1.py
# Assignment 1: Design Your Own Class
# Here we model a Smartphone with inheritance to explore OOP concepts

class Smartphone:
    def __init__(self, brand, model, battery=100, storage=128):
        """
        Initialize a Smartphone with:
        - brand: brand of the phone
        - model: model name
        - battery: battery percentage (default 100)
        - storage: storage space in GB (default 128GB)
        """
        self.brand = brand
        self.model = model
        self.battery = battery
        self.storage = storage
        self.apps = []

    def install_app(self, app_name):
        """
        Install an app if there's enough storage.
        """
        if self.storage >= 1:
            self.apps.append(app_name)
            self.storage -= 1  # Assume each app takes 1GB
            print(f"App '{app_name}' installed on {self.model}. 📱")
        else:
            print("Not enough storage to install the app.")

    def charge(self):
        """
        Charge the smartphone battery to full.
        """
        self.battery = 100
        print(f"{self.model} is fully charged! 🔋")

    def use(self, hours):
        """
        Use the phone for a certain number of hours. Battery drains.
        """
        usage = hours * 10  # 10% battery per hour
        if self.battery >= usage:
            self.battery -= usage
            print(f"Used {self.model} for {hours} hour(s). 🔄")
        else:
            print(f"Not enough battery to use for {hours} hour(s). Please charge.")

    def get_status(self):
        """
        Print current battery level, storage, and installed apps.
        """
        print(f"{self.brand} {self.model} -> Battery: {self.battery}%, Storage: {self.storage}GB")
        print(f"Installed apps: {', '.join(self.apps) if self.apps else 'None'}")

# Inheritance layer: A Smartwatch inherits from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model):
        super().__init__(brand, model, battery=80, storage=32)
        self.heart_rate = 0

    def track_heart_rate(self, rate):
        self.heart_rate = rate
        print(f"{self.model} is tracking heart rate: {rate} bpm ❤️")

# Demonstration
if __name__ == "__main__":
    phone = Smartphone("Pixel", "8 Pro")
    watch = Smartwatch("Samsung", "Galaxy Watch 6")

    phone.get_status()
    phone.install_app("Instagram")
    phone.use(3)
    phone.get_status()

    watch.get_status()
    watch.track_heart_rate(72)
    watch.install_app("Health Monitor")
    watch.get_status()
