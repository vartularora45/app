from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databasesetup import Base, Restaurant, MenuItem

app = Flask(__name__)

# Set up the database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Define the route
@app.route('/')
@app.route('/hello')
def hello_world():
    restaurant = session.query(Restaurant).first()
    if not restaurant:
        return "No restaurant found."
    
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    output = ''
    for item in items:
        output += item.name + '<br>'
    
    return output

# Run the Flask app
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
