"""Bars Command Line Utility."""
import sys
from loguru import logger
import click
from turn_bot.config_local import DEBUG_LEVEL
logger.enable(__package__)
logger.remove(0)


@click.command()
@click.version_option()
def prod_server():
    """Execute Default Function."""
    from turn_bot.waitress_server import main
    logger.add(sys.stderr, colorize=True, level=DEBUG_LEVEL)
    logger.info("Log Level set to " + DEBUG_LEVEL)
    main()


@click.command()
@click.version_option()
def dev_server():
    """Execute Dev Server Function."""
    from turn_bot.webhooks import main
    logger.add(sys.stderr, colorize=True, level=DEBUG_LEVEL)
    logger.info("Log Level set to " + DEBUG_LEVEL)
    main()
