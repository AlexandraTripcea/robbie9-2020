from time import sleep


class ImageAnalysisService:

    def upload_image(self, image_filename: str):
        print("Upload image...")
        sleep(0.25)

    def detect_traffic_light(self, image_filename: str) -> bool:
        print("Detect traffic light...")
        sleep(0.25)
        return False
