// Use djinn namespace
if (djinn == undefined) {
  var djinn = {}
}


djinn.core = {

  // Timeout in milliseconds for message box.
  MESSAGE_TIMEOUT: 3000
};


$(document).ready(function() {

    console.log($(".message.alert"));

    // Hide messages if need be
    setTimeout("$('.message.alert').hide('slow')", djinn.core.MESSAGE_TIMEOUT);
  });
