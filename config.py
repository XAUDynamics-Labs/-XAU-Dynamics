import os
import logging

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | XAU-PIPELINE | %(message)s'
)
logger = logging.getLogger(__name__)

# Enterprise Configurations
AZURE_COSMOS_URI = os.getenv("AZURE_COSMOS_URI", "https://xau-dynamics-db.documents.azure.com:443/")
AZURE_COSMOS_KEY = os.getenv("AZURE_COSMOS_KEY", "MOCKED_AZURE_COSMOS_PRIMARY_KEY_FOR_SECURITY")
DATABASE_NAME = "XAUDynamicsDB"
CONTAINER_NAME = "MarketTicks"

# High-Frequency Data Feeds (OANDA / MetaTrader WebSockets simulated)
GOLD_FEED_URL = os.getenv("GOLD_FEED_URL", "wss://stream-api.xau-dynamics.io/v3/gold")
RETRY_DELAY_SECONDS = 5
