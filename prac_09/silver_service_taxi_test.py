"""
Silver service taxi tests
"""

from  prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test drive the silver service taxi"""
    taxi = SilverServiceTaxi('Hummer', 200, 4)
    taxi.drive(100)
