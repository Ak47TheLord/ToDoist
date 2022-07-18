from ..models import TaskBoard


def get_project_context(form, action_url, list_url, title):
    return {
        "title": title,
        "form": {
            "form": form,
            "action_url": action_url,
            "method": "post"
        },
        "actions": [
            {
                "tag": "a",
                "title": "Back",
                "attrs": [
                    {
                        "name": "class",
                        "value": "btn btn-danger"
                    }, {
                        "name": "href",
                        "value": list_url
                    }
                ],
                "icon": "fa fa-back-arrow"
            }, {
                "tag": "button",
                "title": "Submit",
                "attrs": [
                    {
                        "name": "class",
                        "value": "btn btn-success"
                    }, {
                        "name": "type",
                        "value": "submit"
                    }
                ],
                "icon": "fa fa-plus"
            },
        ]
    }


def get_task_board(obj):
    status_name = ["Urgent", "High", "Medium", "Low"]
    for status in status_name:
        task_board = TaskBoard.objects.create(title=status, project=obj)
