from canvasAPI import Student, Course, Assignments
import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.message("onboard")
def message_onboard(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Hey there <@{message['user']}>! :wave:" 
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "We're excited to get started with you! Eddy helps you to save valuble time through integrating with your e-learning platform right here within Slack. Here are just few things which you will be able to do:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "• Receive information about courses \n • Never miss a quizz  \n • Stay on top of Assignments \n • Have all your links ready for the day  "
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "But before you can do all these fantastic things, we need to connect your Canvas to me. Simply click the button below:"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Connect account",
						"emoji": True
					},
					"value": "click_me_123",
                    "action_id": "onboard_click"
				}
			]
		}
	],
        text=f"Hey there <@{message['user']}>!"
    )

@app.message("testing1")
def testing_one(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
	"title": {
		"type": "plain_text",
		"text": "Input your Token",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "Go to your E-Learning platform and generate your token in your profile settings.\n Hit Submit and close this window when you are done. ",
				"emoji": True
			},
			"element": {
				"type": "plain_text_input",
				"multiline": True
			}
		}
	]
}
	],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("onboard_click")
def action_onboard_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> onboarding")



@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 4000)))

# {
# 	"title": {
# 		"type": "plain_text",
# 		"text": "Input your Token",
# 		"emoji": true
# 	},
# 	"submit": {
# 		"type": "plain_text",
# 		"text": "Submit",
# 		"emoji": true
# 	},
# 	"type": "modal",
# 	"close": {
# 		"type": "plain_text",
# 		"text": "Cancel",
# 		"emoji": true
# 	},
# 	"blocks": [
# 		{
# 			"type": "input",
# 			"label": {
# 				"type": "plain_text",
# 				"text": "Go to your E-Learning platform and generate your token in your profile settings.\n Hit Submit and close this window when you are done. ",
# 				"emoji": true
# 			},
# 			"element": {
# 				"type": "plain_text_input",
# 				"multiline": true
# 			}
# 		}
# 	]
# }
