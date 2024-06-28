import discourier.kinds
import discourier.logger
import discourier.util
import discourier.webhook

logger = discourier.logger.Logger()

url = discourier.util.lookup("url")
usr = discourier.util.lookup("name")
pfp = discourier.util.lookup("avatar")
lvl = discourier.util.lookup("level")
fmt = discourier.util.lookup("format")
ttl = discourier.util.lookup("title")
msg = discourier.util.lookup("message")

logger.debug(f"Webhook endpoint is {url}")
logger.debug(f"Username for payload is {usr}")
logger.debug(f"Avatar profile for payload is {pfp}")
logger.debug(f"Webhook level is {lvl}")
logger.debug("Github notification format is ", end="")

if fmt:
  logger.debug("enabled.")
else:
  logger.debug("disabled.")

logger.debug(f"Title for payload is {ttl}")
logger.debug(f"Payload message is {msg}")

kind = discourier.kinds.WebhookMessage

if lvl not in discourier.kinds.WEBHOOK_KINDS:
  logger.warning(f"Unknown message kind {lvl}")
  logger.warning("Using a plain payload.")
else:
  kind = discourier.kinds.WEBHOOK_KINDS[lvl]

try:
  hook = discourier.webhook.Webhook(url, user=usr, avatar=pfp)
  res = hook.wire(kind(msg, fmt=fmt), title=ttl)

  if res.ok():
    logger.notice("Webhook payload was delivered successfully.")
  else:
    logger.error(f"Received unexpected error {res.code}: {res.msg}.")

except discourier.webhook.ErrorWebhookTimeout:
  logger.error("Connection timed out while trying to connect to Discord.")
except discourier.webhook.ErrorRequestProblem as err:
  logger.error(f"There is likely an issue with your settings for this Action.")
  logger.error(f"Received error code {err.code}: {err.msg}.")
