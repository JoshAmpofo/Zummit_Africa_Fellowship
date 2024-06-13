import numpy as np
import pandas as pd
import pickle
import streamlit

# load saved model
with open('hoteller_model.sav', 'rb') as f:
    lmodel = pickle.load(f)
    
# load hotel_df
hotel_df = pd.read_csv('hotel_df.csv')

# Streamlit app
def main():
    streamlit.title("Hoteller")

    user_id = streamlit.text_input("Username")
    city = streamlit.text_input("City")
    num_recommendations = streamlit.number_input("Number of reccommendations", min_value=1, max_value=10, value=5, step=1)

    if streamlit.button("Get Recommendations"):
        try:
            recommendations = hotel_recommendations(lmodel, user_id, city, num_recommendations=num_recommendations)
            if recommendations:
                streamlit.write(f"Recommending hotels for {user_id} in {city}:")
                for index, recommendation in enumerate(recommendations, start=1):
                    streamlit.markdown(f"{index}. **{recommendation}**") 
            else:
                streamlit.write("No recommendations found.")
        except ValueError as e:
            streamlit.write(str(e))
        except IndexError:
            streamlit.write(str(e))
            
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

if __name__ == '__main__':
    main()
