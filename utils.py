def validate_coordinates(latitude: float, longitude: float) -> bool:
    """
    Validates if the given latitude and longitude are within reasonable ranges.

    Args:
        latitude (float): Latitude value to validate.
        longitude (float): Longitude value to validate.

    Returns:
        bool: True if both latitude and longitude are valid, False otherwise.
    """
    if not (-90 <= latitude <= 90):
        return False
    if not (-180 <= longitude <= 180):
        return False
    return True