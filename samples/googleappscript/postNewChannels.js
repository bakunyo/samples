function postNewChannels() {
  var prop = PropertiesService.getScriptProperties().getProperties();

  var slackApp = SlackApp.create(prop.token);
  var response = slackApp.channelsList(true);
  var targetChannel = "";

  var span = 60 * 60 * 1000;
  var checkFrom = new Date(Date.now() - span);
  var newChannels = [];
  var created;
  for each(var channel in response.channels) {
    created = new Date(channel.created * 1000);
    if (checkFrom > created) { continue; }

    newChannels.push("#" + channel.name);
  }

  if (newChannels.length === 0) { return false; }

  var message = newChannels.join("\n");
  slackApp.chatPostMessage(targetChannel, message, { username : "New Channels", icon_emoji : ":octopus:", parse: "full" });
}
