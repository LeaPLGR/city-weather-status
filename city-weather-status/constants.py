import os
import pandas as pd

if "AQI_KEY" not in os.environ:
    from dotenv import load_dotenv

    load_dotenv()

AQI_KEY = os.environ.get("AQI_KEY")
AQI_URL_FEED = "https://api.waqi.info/feed/"
AQI_URL_MAP = "https://api.waqi.info/v2/map/bounds"


AQI_LEVELS = pd.DataFrame(
    {
        "AQI": ["0-50", "50-100", "100-150", "150-200", "200-300", "300-"],
        "Air pollution level": [
            "Good",
            "Moderate",
            "Unhealthy for Sensitive Groups",
            "Unhealthy",
            "Very Unhealthy",
            "Hazardous",
        ],
        "Health Implications": [
            "Air quality is considered satisfactory, and air pollution poses little or no risk.",
            "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.",
            "Members of sensitive groups may experience health effects. The general public is not likely to be affected.",
            "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
            "Health warnings of emergency conditions. The entire population is more likely to be affected.",
            "Health alert: everyone may experience more serious health effects.",
        ],
        "Healthy persons": [
            "Continue with normal activities",
            "Continue with normal activities",
            "Continue with normal activities",
            "Reduce prolonged or strenuous outdoor physical exertion",
            "Avoid prolonged or strenuous outdoor physical exertion",
            "Minimise outdoor activity",
        ],
        "Elderly, pregnant women, children": [
            "Continue with normal activities",
            "Continue with normal activities",
            "Minimise prolonged or strenuous outdoor physical exertion",
            "Minimise prolonged or strenuous outdoor physical exertion",
            "Minimise outdoor activity",
            "Avoid outdoor activity",
        ],
        "Persons with chronic lung disease or heart disease": [
            "Continue with normal activities",
            "Continue with normal activities",
            "Minimise prolonged or strenuous outdoor physical exertion",
            "Avoid prolonged or strenuous outdoor physical exertion",
            "Avoid outdoor activity",
            "Avoid outdoor activity",
        ],
    }
)

# https://aqicn.org/json-api/doc/#api-City_Feed
# https://aqicn.org/data-platform/token-confirm/91ac4eba-b44f-44bb-a2a9-7e357c7bc227
