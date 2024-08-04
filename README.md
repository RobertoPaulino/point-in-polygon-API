# 🎯 point-in-shapefile-API

Welcome to my **point-in-shapefile-API**, This Python-based API, powered by **Flask**, **GeoPandas**, and the **Google Maps API**, is my solution for determining whether an address falls within a specified polygon shape.

## 🚀 Features

- **Single GET Method**: Send an address, get back a JSON response.
- **Geo-coordinates Calculation**: Automatically fetches the coordinates of the given address using Google's API.
- **Polygon Check**: Verifies if the coordinates fall within the specified shapefile's polygon.

## 📦 Installation


### Step 1: Clone the Repository

```bash
git clone https://github.com/RobertoPaulino/point-in-shapefile-API.git
cd point-in-shapefile-API
```

### Step 2: Set Up Your Environment

You'll need to create a `.env` file in the root directory to store your Google Maps API key:

```plaintext
API_KEY=your_api_key_here
```

If you want more information on the googlemaps API make sure to read their [GitHub repository](https://github.com/googlemaps/google-maps-services-python), it has all the information and links needed to understand their API.

### Step 3: Organize Your Shapefiles

Make sure you have a folder called `shapefile` in the root directory. This folder will contain the shapefiles you want to use. For example:

```
point-in-shapefile-API/
├── shapefile/
│   ├── your_shapefile.shp
│   ├── your_shapefile.dbf
│   ├── your_shapefile.shx
│   └── ... (other related files)
└── ...
```

**Pro Tip:** Start with the shapefiles from [USDA Rural Development Property Eligibility](https://catalog.data.gov/dataset/usda-rural-development-property-eligibility-sfh-mfh) to test, you can easily switch to other shapefiles of similar structure later.

### Step 4: Install Dependencies

Ensure you have Python 3.7+ and pip installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

Time to put our API to work! Here's how to do it:

### Run the API

Simply execute the following command:

```bash
python app.py
```

Your API should now be running at `http://localhost:5000`. 

### Make a GET Request

Use your favorite tool to make a request, you can also use your favorite browser to take a look at the JSON response:

```
http://localhost:5000//get-eligibility/address=1600+Pennsylvania+Ave+NW,+Washington,+DC+20500
```

### Response

The API will return a JSON response containing:

- **address**: The input address.
- **coordinates**: Latitude and longitude of the address.
- **is_eligible**: Whether the address is inside the polygon, currently in the USDA eligibility data anything inside the polygon is not eligible,
you can make changes to the response and variables in the code to fit your project

```json
{
  "address": "address=1600+Pennsylvania+Ave+NW,+Washington,+DC+20500",
  "coordinates": [
    -77.0363948,
    38.89764
  ],
  "is_eligible": "not eligible"
}

```

## 🛠️ Customization

Want to tweak the code to fit your needs? Feel free to change the names of variables and functions for better readability in your project. 🛠️👨‍💻

## 🤝 Contributing
Contributions are always welcome! Whether it's a bug report, new feature, or a piece of advice, we appreciate your input.

### How to Contribute

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m 'Add some awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the Creative Commons Zero (CC0) [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [GeoPandas](https://geopandas.org/)
- [Google Maps API](https://developers.google.com/maps)

## 🌟 Final Words

Happy coding, and may your polygons be ever accurate! 🧙‍♂️✨
