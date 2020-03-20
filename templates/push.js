var push = require('web-push');

let vapidKeys = {
    publicKey: 'BOK25RgJa6YgBgnybtBOU1xfa14taMwiDfa4asMkA9uzl507OyEYqriyxXaduqAgPcnn90w4Vc--nCNuwkLxUIA',
    privateKey: '8Q0H_WVvyhN8I9eDdWGj0aWp5RgwcpEHJUOoIDqJXv8'
  }

push.setVapidDetails('mailto:test@code.co.uk', vapidKeys.publicKey, vapidKeys.privateKey)

let sub = {};
push.sendNotification(sub, 'test message')