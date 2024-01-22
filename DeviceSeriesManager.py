import requests
import subprocess
import readConfig
import time

class DeviceSeriesManager:
    def __init__(self, common_api_url):
        self.common_api_url = common_api_url
        self.common_headers = {
            'Content-Type': 'application/json'
        }

    def get_oauth_token(self):
        oauth2l_command = '~/go/bin/oauth2l header --json /home/doughfactory/Downloads/secret.json https://www.googleapis.com/auth/device-certification.frontend email --refresh'
        result = subprocess.run(oauth2l_command, shell=True, capture_output=True, text=True)
        return result.stdout.strip().replace('Authorization: ', '')

    def create_device_series(self, payload):
        oauth_header = self.get_oauth_token()
        self.common_headers['Authorization'] = oauth_header

        response = requests.post(self.common_api_url, headers=self.common_headers, json=payload)

        print(response.status_code)
        print(response.json())

    def upload_device_models(self, api_url, configurations):
        oauth_header = self.get_oauth_token()
        self.common_headers['Authorization'] = oauth_header

        for config in configurations:
            response = requests.post(api_url, headers=self.common_headers, json=config)
            print(response.status_code)
            print(response.json())
            time.sleep(5)  # Pause for 5 seconds between requests

if __name__ == '__main__':
    # constructor usage:
    common_api_url = 'https://autopush-saltmine-pa.sandbox.googleapis.com/v2/deviceSeries'
    device_manager = DeviceSeriesManager(common_api_url)

    # Payload for creating a new series
    create_series_payload = readConfig.read_create_series_json()
    device_manager.create_device_series(create_series_payload)

    # Configurations for model creation and model update request
    model_api_url = 'https://autopush-saltmine-pa.sandbox.googleapis.com/v2/deviceSeries/2054194/deviceModels:upload'
    model_configurations = readConfig.read_json()
    device_manager.upload_device_models(model_api_url, model_configurations)
