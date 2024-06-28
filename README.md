# Discord Webhook

GitHub Action for writing to a Discord webhook.

## Inputs

### `url`

**Required** The webhook endpoint to write to.

### `message`

**Required** The message contents to send.

### `name`

The username to identify as with Discord.

### `avatar`

The URL of the avatar to use for the message.

### `level`

The notification level to use.

### `title`

Set the title of the notification.

### `format`

Apply the standard message template.

## Example usage

```yaml
uses: uplime/discord-webhook@v1.1
with:
  url: https://discord.com/api/webhooks/123457890/correct-horse-battery-staple
  level: error
  message: "I'm afraid I can't do that, Dave."
  format: yes
```
