import logging

logging.basicConfig(
    level=logging.INFO
)

logging.info("Deployment started")
logging.warning("High CPU")
logging.error("Deployment failed")