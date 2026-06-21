class Query:
    def __init__(self):
        self.columns = []
        self.table = None
        self.where_conditions = []
        self.order = None
        self.limit_value = None
    
    def select(self, *columns):
        self.columns = columns
        return self
    
    def from_(self, table):
        self.table = table
        return self
    
    def where(self, where_conditions):
        self.where_conditions.append(where_conditions)
        return self
    
    def order_by(self, order, desc = False):
        if desc == True:
            direction = "DESC"
        else:
            direction = "ASC"
        self.order = order
        self.order_direction = direction
        return self
    
    def limit(self, value):
        self.limit_value = value
        return self
    
    def build(self):
        if not self.table:
            raise ValueError("Table doesn't exist")
        columns = ", ".join(self.columns) if self.columns else "*"
        query = f"SELECT {columns} FROM {self.table}"
        if self.where_conditions:
            query += " WHERE " + " AND ".join(self.where_conditions)
        if self.order:
            query += f" ORDER BY {self.order} {self.order_direction}"
        if self.limit_value is not None:
            query += f" LIMIT {self.limit_value}"
        return query

q = (Query()
    .select("id", "name", "amount")
    .from_("orders")
    .where("status = 'paid'")
    .where("amount > 100")
    .order_by("amount", desc=True)
    .limit(10))

print(q.build())


        

    
        

    