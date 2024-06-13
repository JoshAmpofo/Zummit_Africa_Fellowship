import os
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# search filepath
def find_file(filename, search_path='.'):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"{filename} not found in the directory tree.")


# find file
model_path = find_file('hoteller_model.sav')
data_path = find_file("hotel_df.csv")


# load saved model
with open(model_path, 'rb') as f:
    lmodel = pickle.load(f)
    
# load hotel_df
hotel_df = pd.read_csv(data_path)

            
def hotel_recommendations(model, user_id, city, user_features=None, item_features=None, num_recommendations=10):
    """
    Recommends hotels for a given user based on the LightFM model and their city.

    Args:
        model: The trained LightFM model.
        user_id: The string ID of the user for whom to generate recommendations.
        city: The city of the user for whom to generate recommendations.
        user_features: User features matrix (optional).
        item_features: Item features matrix (optional).
        num_recommendations: Number of recommendations to return (default: 10).

    Returns:
        A list of recommended hotel IDs.
    """
    # Check if user_id exists in the dataset
    user_idx = hotel_df[hotel_df['user_id'] == user_id]
    
    if not user_idx.empty:
        user_idx = user_idx.index[0]
    else:
        # If user_id does not exist, create a default user index
        user_idx = 'default_user'

    # Filter hotels based on the user's city
    city_hotels = hotel_df[hotel_df['user_city'] == city]
    if city_hotels.empty:
        raise(f"No hotels found for the city {city}.")

    item_ids = city_hotels['hotel_id'].unique()
    num_items = len(item_ids)

    # Predict scores for all items for the given user
    if user_idx == 'default_user':
        user_ids = np.zeros(num_items)  # Use zero as a placeholder for default user index
    else:
        user_ids = np.repeat(user_idx, num_items)
    
    item_indices = np.arange(num_items)

    scores = lmodel.predict(user_ids, item_indices) #user_features=user_features_lookup, item_features=item_features)

    # Get the indices of the top N items sorted by predicted scores in descending order
    top_items = np.argsort(-scores)[:num_recommendations]

    # Return the list of recommended hotel IDs
    return item_ids[top_items].tolist()

# streamlit app
def main():
    # style title
    st.set_page_config(page_title='Hoteller', page_icon="🏨", layout="wide")
    # give page a title
    st.title("Hotels with Hoteller 🏨")
    # user input fields
    user_id = st.text_input("Username", placeholder="Enter your username")
    city = st.text_input("City", placeholder="Enter your city", help="City you're looking for hotels")
    num_recommendations = st.number_input("Number of recommendations", min_value=1, max_value=10, value=5, step=1)

    if st.button("Recommend"):
        try:
            recommendations = hotel_recommendations(lmodel, user_id, city, num_recommendations=num_recommendations)
            if recommendations:
                st.write(f"Recommending hotels for {user_id} in {city}:")
                for index, recommendation in enumerate(recommendations, start=1):
                    st.markdown(f"{index}. **{recommendation}**") 
            else:
                st.write("No recommendations found.")
        except ValueError as e:
            st.write(str(e))
        except IndexError:
            st.write(str(e))

if __name__ == '__main__':
    main()
