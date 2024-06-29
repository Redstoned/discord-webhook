import discourier.kinds
import discourier.logger
import discourier.util
import discourier.webhook
import sys

logger = discourier.logger.Logger()

url = discourier.util.lookup("url")
msg = discourier.util.lookup("message")
user = discourier.util.lookup("name")
pfp = discourier.util.lookup("avatar")
level = discourier.util.lookup("level")
title = discourier.util.lookup("title")
do_format = discourier.util.lookup("format")
do_fail = discourier.util.lookup("fail")

logger.debug(f"Webhook endpoint is {url}.")
logger.debug(f"Username for payload is {user}.")
logger.debug(f"Avatar profile for payload is {pfp}.")
logger.debug(f"Webhook level is {level}.")
logger.debug(f"Title for payload is {title}.")
logger.debug(f"Payload message is {msg}.")
logger.debug("Github notification format is ", end="")

if do_format:
  logger.debug("enabled.")
else:
  logger.debug("disabled.")

logger.debug("Notification will ", end="")

if not do_fail:
  logger.debug("not ", end="")

logger.debug("exit with failure.")
kind = discourier.kinds.WebhookMessage

if level not in discourier.kinds.WEBHOOK_KINDS:
  logger.warning(f"Unknown message kind {level}")
  logger.warning("Using a plain payload.")
else:
  kind = discourier.kinds.WEBHOOK_KINDS[level]

try:
  hook = discourier.webhook.Webhook(url, user=user, avatar=pfp)
  res = hook.wire(kind(msg, fmt=do_format), title=title)

  if res.ok():
    logger.notice("Webhook payload was delivered successfully.")

    if do_fail:
      sys.exit(1)
  else:
    logger.error(f"Received unexpected error {res.code}: {res.msg}.")
    sys.exit(1)
except discourier.webhook.ErrorWebhookTimeout:
  logger.error("Connection timed out while trying to connect to Discord.")
  sys.exit(1)
except discourier.webhook.ErrorRequestProblem as err:
  logger.error(f"There is likely an issue with your settings for this Action.")
  logger.error(f"Received error code {err.code}: {err.msg}.")
  sys.exit(1)
