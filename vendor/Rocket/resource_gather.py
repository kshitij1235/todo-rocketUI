import os
from vendor.Rocket.Log import log

def get_resource_images(image_name: str)->str:
    """
    Returns the actual path of the image 
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.normpath(os.path.join(current_directory, '..', '..'))
    image_path = os.path.join(project_root, 'resources', 'images', image_name)

    log(f"bootstraping for resource :  {image_path}")  

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image '{image_name}' not found at path: {image_path}")

    return image_path
