from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)
# Database connection
# from pymongo.mongo_client import MongoClient
 # Create a new client and connect to the server
# client = MongoClient(uri)
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     firstName = Column(String)
#     lastName = Column(String)
#     email = Column(String)
#     phone = Column(Integer)
#     password = Column(String)

# class UserCreate(BaseModel):
#     firstName: str
#     lastName: str
#     email: str
#     phone: int
#     password: str

# class UserUpdate(BaseModel):
#     firstName: str
#     lastName: str
#     email: str
#     phone: int
#     password: str

# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/users")
# def get_users(db = Depends(get_db)):
#     users = db.query(User).all()
#     return {"users": users}

# @app.get("/users/{user_id}")
# def get_user(user_id: int, db = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user:
#         return {"user": user}
#     else:
#         return {"message": "User not found"}

# @app.post("/users")
# def create_user(user: UserCreate, db = Depends(get_db)):
#     db_user = User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return {"message": "User created successfully"}

# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: UserUpdate, db = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user:
#         for field, value in user.dict(exclude_unset=True).items():
#             setattr(db_user, field, value)
#         db.commit()
#         db.refresh(db_user)
#         return {"message": "User updated successfully"}
#     else:
#         return {"message": "User not found"}

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#         return {"message": "User deleted successfully"}
#     else:
#         return {"message": "User not found"}
    

# class Product(BaseModel):
#    id: int
#    name: str
#    price: float
#    description: str

# products = []

# # Create a route to add a new product
# @app.post("/products/", response_model=Product)
# def create_product(product: Product):
#     products.append(product)
#     return product

# # Create a route to get a list of all products
# @app.get("/products/", response_model=List[Product])
# def read_products():
#     return products

# # Create a route to get a single product by ID
# @app.get("/products/{product_id}", response_model=Product)
# def read_product(product_id: int):
#     if product_id < 0 or product_id >= len(products):
#         raise HTTPException(status_code=404, detail="Product not found")
#     return products[product_id]

# # Create a route to update a product by ID
# @app.put("/products/{product_id}", response_model=Product)
# def update_product(product_id: int, updated_product: Product):
#     if product_id < 0 or product_id >= len(products):
#         raise HTTPException(status_code=404, detail="Product not found")
#     products[product_id] = updated_product
#     return updated_product

# # Create a route to delete a product by ID
# @app.delete("/products/{product_id}", response_model=Product)
# def delete_product(product_id: int):
#     if product_id < 0 or product_id >= len(products):
#         raise HTTPException(status_code=404, detail="Product not found")
#     deleted_product = products.pop(product_id)
#     return deleted_product
