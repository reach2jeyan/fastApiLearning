from datetime import datetime, timedelta

userList = {
            'explanation': "This is a GET api method request that you can use to fetch any data from the database if the api supports returning that data. If the api design supports it, you can also pass a query param to query only the user you want",
            'excercise': "Try to pass, the userId that you see in the response as query parameter? ",
            'userDetails': [
                {
                    "id": 1,
                    "name": "sonz",
                    "age": 32,
                    "city": "bangalore",
                    "address": "hsr",
                    "dob": datetime.now() - timedelta(days=6)
                },
                {
                    "id": 2,
                    "name": "aastha",
                    "age": 26,
                    "city": "M G Road",
                    "address": "hsr",
                    "dob": datetime.now() - timedelta(days=5)
                },
                {
                    "id": 3,
                    "name": "saurav",
                    "age": 40,
                    "city": "bangalore",
                    "address": "Koramangala",
                    "dob": datetime.now() - timedelta(days=4)
                },
                {
                    "id": 4,
                    "name": "divyanjali",
                    "age": 30,
                    "city": "Lucknow",
                    "address": "JankiPuram",
                    "dob": datetime.now() - timedelta(days=3)
                },
                {
                    "id": 5,
                    "name": "Rupam",
                    "age": 27,
                    "city": "Goa",
                    "address": "Sarjapur",
                    "dob": datetime.now() - timedelta(days=2)
                },
                {
                    "id": 6,
                    "name": "Avinash",
                    "age": 32,
                    "city": "bangalore",
                    "address": "Bellandur",
                    "dob": datetime.now() - timedelta(days=1)
                },
            ]
        }

userCity = {
        'explanation': " This example is to learn, array inside a key value pair. In this excercise, query the city of sonzz that should return you the array. Also, write a test, to see if the array contains something called \"puranpur\"",
        'userDetails': [
            {
                "name": "sonz",
                "age": 32,
                "city": ["bangalore","Lucknow","puranpur","barielly"],
                "address": "hsr",
                "dob": datetime.now() - timedelta(days=6)
            },
            {
                "name": "aastha",
                "age": 26,
                "city":["bangalore","Delhi"],
                "address": "MG ROAD",
                "dob": datetime.now() - timedelta(days=5)
            },
            {
                "name": "saurav",
                "age": 40,
                "city": ["bangalore","chandigarh"],
                "address": "Koramangala",
                "dob": datetime.now() - timedelta(days=4)
            },
            {
                "name": "divyanjali",
                "age": 30,
                "city": ["bangalore","Lucknow"],
                "address": "JankiPuram",
                "dob": datetime.now() - timedelta(days=3)
            },
            {
                "name": "Rupam",
                "age": 27,
                "city": ["bangalore","Lucknow", "goa"],
                "address": "Sarjapur",
                "dob": datetime.now() - timedelta(days=2)
            },
            {
                "name": "Avinash",
                "age": 32,
                "city": ["bangalore"],
                "address": "Bellandur",
                "dob": datetime.now() - timedelta(days=1)
            },
        ]
    }