class Employee:
    def __init__(self: "Employee", farmer_id, farmer_pos) -> None:
        self.farmer_id = farmer_id
        self.farmer_pos = farmer_pos

    def set_farmer_pos(self: "Employee", farmer_pos: str) -> None:
        self.farmer_pos = farmer_pos

    def get_farmer_pos(self: "Employee") -> str:
        return self.farmer_pos

    def set_farmer_id(self: "Employee", farmer_id: int) -> None:
        self.farmer_id = farmer_id

    def get_farmer_id(self: "Employee") -> int:
        return self.farmer_id
