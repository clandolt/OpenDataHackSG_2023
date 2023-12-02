
# Frontend Observer
class FrontendObserver:
    def update(self, data):
        print(f"Received data in frontend: {data}")
        # Perform actions based on received data


# Backend Observer
class BackendObserver:
    def update(self, data):
        print(f"Received data in backend: {data}")
        # Process data and take necessary actions
