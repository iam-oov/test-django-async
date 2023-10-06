#!/bin/bash
watch -d '/usr/sbin/rabbitmqctl list_queues -p rabbitmq_app name messages messages_ready messages_unacknowledged consumers| sort'