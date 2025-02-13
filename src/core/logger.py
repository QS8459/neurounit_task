import logging

logger = logging.getLogger(
    name="NEURON",
)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter("%(name)s_%(levelname)s: %(asctime)s - %(message)s", datefmt="%Y-%m-%dT%H:%M:%S"))


logger.addHandler(console_handler)

