# Airbnb Listings Dataset - Austin, TX
The Airbnb Listings dataset contains the complete collection of Airbnb listings in Austin, Texas. This dataset provides valuable insights into the details of each listing that is hosted in Austin, TX. The listings dataset is descriptive towards the layout, location, and amenities of each respective listing.

Preprocessing measures were taken in order to amplify the features of importance from the original raw file. These measures can be sorted into two groups - amplifying existing features and feature removal. 

## Features and Description
The listings dataset includes the following key features:



| Number | Field                  | Type    | Description                                                                                           |
|--------|------------------------|---------|-------------------------------------------------------------------------------------------------------|
| 1      | Id                     | Integer | Airbnb's unique identifier for the listing.                                                           |
| 2      | Listing_url            | Text    | URL of the listing.                                                                                   |
| 3      | Scrape_id              | Integer | Inside Airbnb ID of the "Scrape" this listing was part of.                                             |
| 4      | Last_scraped           | Date    | The date and time this listing was last scraped.                                                      |
| 5      | Source                 | Text    | How the listing was found when searching. "Neighborhood search" means that the listing was found by searching the city, while "previous scrape" means that the listing was seen in another scrape performed in the last 65 days. |
| 6      | Name                   | Text    | The name of the listing.                                                                              |
| 7      | Description            | Text    | A detailed description of the listing.                                                                |
| 8      | Neighborhood_overview  | Text    | The host's description of the neighborhood.                                                           |
| 9      | Picture_url            | Text    | The URL to the Airbnb-hosted regular-sized image for the listing.                                      |
| 10     | Host_id                | Integer | Airbnb's unique identifier for the host/user.                                                         |
| 11     | Host_url               | Text    | The Airbnb page for the host.                                                                         |
| 12     | Host_name              | Text    | The name of the host. Usually just the first name(s).                                                 |
| 13     | Host_since             | Date    | The date the host/user was created. For hosts who are Airbnb guests, this could be their guest registration date. |
| 14     | Host_location          | Text    | The host's self-reported location.                                                                    |
| 15     | Host_about             | Text    | A description about the host.                                                                         |
| 16     | Host_response_time     | Text    | The typical host response time. Possible values: "a few days or more," "within a day," "within a few hours," "within an hour." |
| 17     | Host_response_rate     | Integer | The percentage of time the host responds to inquiries on time.                                         |
| 18     | Host_acceptance_rate   | Integer | The rate at which a host accepts booking requests.                                                     |
| 19     | Host_is_superhost      | Boolean | A value determining if the host is considered a Superhost or not.                                      |
| 20     | Host_thumbnail_url     | Text    | The URL of the Airbnb host's thumbnail photo (small version).                                          |
| 21     | Host_picture_url               | Text    | The URL of the Airbnb host's thumbnail photo (medium version).|
| 22     | Host_neighbourhood             | Text    | The neighborhood where the host is located.                                                                                 |
| 23     | Host_listings_count            | Text    | The number of listings the host has (according to Airbnb calculations).                                                     |
| 24     | Host_total_listings_count      | Text    | The total number of listings the host has (according to Airbnb calculations).                                               |
| 25     | Host_verifications             | Text    | An array of all the ways the host has been verified, such as email, phone, government ID, etc.                            |
| 26     | Host_has_profile_pic           | Boolean | A value determining if the host has a profile picture.                                                                      |
| 27     | Host_identity_verified         | Boolean | A value determining if the host has a verified identity.                                                                    |
| 28     | Neighbourhood                  | Text    | The neighborhood where the listing is located.                                                                              |
| 29     | Neighbourhood_cleansed         | Text    | The approximate zip code or town where the listing is located (for non-U.S. locations).                                    |
| 30     | Neighbourhood_group_cleansed   | Text    | The cleansed version of the neighborhood group. Currently, all values are null.                                            |
| 31     | Latitude                       | Integer | The latitude of the listing's location (using the World Geodetic System, WGS84 projection).                                 |
| 32     | Longitude                      | Integer | The longitude of the listing's location (using the World Geodetic System, WGS84 projection).                                |
| 33     | Property_type                  | Text    | The property type of the listing, such as house, guesthouse, boat, etc.                                                     |
| 34     | Room_type                      | Text    | The room type of the listing. Possible values: "Entire home/apt," "Private room," "Hotel room," "Shared room."              |
| 35     | Accommodates                   | Integer | The maximum number of guests the listing can accommodate.|
| 36     | Bathrooms                      | Integer | The number of bathrooms in the listing.                                                                                     |
| 37     | Bathrooms_text                 | Text    | A textual description of the number of bathrooms in the listing.                                                           |
| 38     | Bedrooms                       | Integer | The number of bedrooms in the listing.                                                                                      |
| 39     | Beds                           | Integer | The number of beds in the listing.                                                                                          |
| 40     | Amenities                      | Text    | An array of all the amenities available at the listing, such as TV, Wi-Fi, air conditioning, etc.                          |
| 41     | Price                          | Integer | The price per night of booking or reservation.                                                                              |
| 42     | Minimum_nights                 | Integer | The minimum number of nights required for a stay at the listing.                                                            |
| 43     | Maximum_nights                 | Integer | The maximum number of nights allowed for a stay at the listing.                                                             |
| 44     | Minimum_minimum_nights         | Integer | The smallest minimum_night value from the calendar (looking 365 nights into the future).                                    |
| 45     | Maximum_minimum_nights         | Integer | The largest minimum_night value from the calendar (looking 365 nights into the future).                                     |
| 46     | Minimum_maximum_nights         | Integer | The smallest maximum_night value from the calendar (looking 365 nights into the future).                                    |
| 47     | Maximum_maximum_nights         | Integer | The largest maximum_night value from the calendar (looking 365 nights into the future).                                     |
| 48     | Minimum_nights_avg_ntm         | Numeric | The average minimum_night value from the calendar (looking 365 nights into the future).                                    |
| 49     | Maximum_nights_avg_ntm         | Numeric | The average maximum_night value from the calendar (looking 365 nights into the future).                                    |
| 50     | Calendar_updated               | Date    | Indicates how long ago the calendar for the listing was last updated.                                                       |
| 51     | Has_availability               | Boolean | A value determining if the listing has availability.                                                                        |
| 52     | Availability_30                | Integer | The number of nights available in the next (or last) 30 days.                                                              |
| 53     | Availability_60                | Integer | The number of nights available in the next (or last) 60 days.                                                              |
| 54     | Availability_90                | Integer | The number of nights available in the next (or last) 90 days.                                                              |
| 55     | Availability_365               | Integer | The number of nights available in the next (or last) 365 days.|
| 56     | Calendar_last_scraped          | Date    | The date of the latest calendar web scraping from the Airbnb website.                                                      |
| 57     | Number_of_reviews              | Integer | The total number of reviews the listing has received.                                                                      |
| 58     | Number_of_reviews_ltm          | Integer | The number of reviews the listing has received in the last 12 months.                                                      |
| 59     | Number_of_reviews_l30d         | Integer | The number of reviews the listing has received in the last 30 days.                                                         |
| 60     | First_review                   | Date    | The date of the first/oldest review for the listing.                                                                       |
| 61     | Last_review                    | Date    | The date of the last/newest review for the listing.                                                                        |
| 62     | Review_scores_rating           | Integer | The score indicating how guests felt overall during their stay.                                                            |
| 63     | Review_scores_accuracy         | Integer | The score indicating how guests felt that the listing page represented the space accurately.                                |
| 64     | Review_scores_cleanliness      | Integer | The score indicating how guests felt that the space was clean and tidy during their stay.                                   |
| 65     | Review_scores_checkin          | Integer | The score indicating how guests felt that the check-in process went smoothly.                                              |
| 66     | Review_scores_communication    | Integer | The score indicating how guests felt that the host communicated effectively before and during their stay.                   |
| 67     | Review_scores_location         | Integer | The score indicating how guests felt about the location/neighborhood of the listing and its proximity to attractions.      |
| 68     | Review_scores_value            | Integer | The score indicating how guests felt about the overall value of the listing for the price.                                 |
| 69     | License                        | Text    | The rental license number for the host.                                                                                    |
| 70     | Instant_bookable               | Boolean | A value determining if instant booking is available for the listing.                                                       |
| 71     | Calculated_host_listings_count | Integer | The total number of listings the host has in the current scrape, in the city/region geography.                            |
| 72     | Calculated_host_listings_count_entire_homes | Integer | The number of entire home/apt listings the host has in the current scrape, in the city/region geography.         |
| 73     | Calculated_host_listings_count_private_rooms | Integer | The number of private room listings the host has in the current scrape, in the city/region geography.              |
| 74     | Calculated_host_listings_count_shared_rooms | Integer | The number of shared room listings the host has in the current scrape, in the city/region geography.                |
| 75     | Reviews_per_month              | Integer | The average number of reviews the listing has received over its lifetime.                                                   |

## Data Files

*  **austin_zip_codes.geojson** This geojson data file represents the coordinates for all the zip codes within Austin, TX. It is not necesary for preprocessing of the listings dataset, but it is impactful for the data exploration and is needed for the listings_exploration.ipynb.

*  **listings_exploration.ipynb** This notebook is where the exploration of the listings dataset takes place. Due to the robust amount of features with its raw import, realizing the impact and potential with the data needed to be done.
  
*  **listings_preprocessing.ipynb** This notebook is where the entire preprocessing is performed on the raw imported listings information. It utilizes various techniques to consolidate, clean, and amplify features of interest for the overall objective and model. Light investigative work is carried out to realize the counts for certain features, and each step is explained accordingly.

*  **processed_listings.csv:** This CSV file contains the latest processed listings data. It was preprocessing solely within the listings_preprocessing.ipynb file. Unnecessary features were removed, locational features were amplfied, and non-numerical data points were converted to either float64 or int64 data points. Unnecessary features are features that were deemed unrelated to the objective and model. Locational features represent the addition of locations of importance around Austin and finding the distance from each listing. The locations of interest were sourced from Austin's tourism website. Additionally, the 30 most popular amenities were calcualted across all the listings, and a check whether or not a listing has each top 30 amenity was added. The final dataframe has a shape of (14345 rows, 86 columns).

  
### Source of the Dataset:
The Airbnb listings dataset for Austin, Texas can be obtained from the official Inside Airbnb website. You can access and download the dataset from the following source: [Inside Airbnb.](http://insideairbnb.com/get-the-data/) This CSV file contains the raw data sourced from insideairbnb. It contains much needed information for the model with feature columns such as longitude, latitude, amenities, host_id, review scores, and more; although, some of the imported features are irrelevant for the objective and model. This file is utilized at the beginning of the listings_preprocessing.ipynb file. In its initial import, the dataframe shape is (14368 rows, 75 columns).

To use the Airbnb listings notebook, please ensure that you have the appropriate file path or access to the dataset.

### Package Versions and Imports

To successfully run the notebook and reproduce the results, ensure that you have the following package versions installed: <br>
pandas version: 1.5.3 <br>
numpy version: 1.25.1 <br>
tqdm version: 4.65.0 <br>
geopy version: 2.3.0 <br>

*  pandas: pandas is a powerful data manipulation and analysis library in Python. It provides easy-to-use data structures and data analysis tools, making it efficient for working with structured data.
*  numpy: numpy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
*  tqdm: tqdm is a visual tool to check the progress of a function. While recommended, it is not necessary for the code, but it is included in the notebook file. Either download and run or comment out its involvement.  
*  geopy: geopy is a helpful package for locational computing in python. It allows developers to locate the longitude and latitude coordinates for locations of interest across the globe.

You can install the required packages using `pip`:  <br>
`!python -m pip install pandas` <br>
`!python -m pip install numpy` <br>
`!python -m pip install tqdm` <br>
`!python -m pip install geopy` <br>


### Getting Started

To get started with the project, follow these steps:

1. Download the Austin, Tx Airbnb listings dataset included as, raw_listings_insideairbnb.csv, or from [Inside Airbnb](http://insideairbnb.com/get-the-data/).
2. Install the required dependencies as mentioned above.
3. Run the project code using your preferred Python environment.

