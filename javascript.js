var items = [
  'amazon', 'github', 'html5', 'mastodon', 'reddit', 'soundcloud', 
  'tox', 'wechat', 'youtube', 'dropbox', 'gitlab', 'instagram', 
  'paypal', 'rss', 'spotify', 'tumblr', 'whatsapp', 'email',
  'google_plus', 'linkedin', 'pdf', 'skype', 'stackoverflow', 'twitter',
  'wikipedia', 'facebook', 'google', 'lock', 'phone', 'slideshare',
  'steam', 'vimeo', 'wire', 'flickr', 'hackernews', 'mail',
  'pinterest', 'snapchat', 'telegram', 'vk', 'wordpress', 'meetup',
  'line', 'lastpass', 'windows', 'digidentity', 'ubuntu', 'bitbucket',
  'apple', 'npm', 'docker', 'symantec', 'yubico', 'keybase',
  'ebay', 'evernote', 'kickstarter', 'yahoo', 'bitcoin', 'bluetooth',
  'ibm', 'yammer', 'android', 'authy'
];

var container = document.querySelector('.icons');
var range = document.querySelector('input[type="range"]');
var number = document.querySelector('input.rangeout');
range.addEventListener('input', function(e){
  number.value = parseInt(e.target.value);
  render(e.target.value);
});

number.addEventListener('input', function(e){
  range.value = parseInt(e.target.value);
  render(e.target.value);
});

var urls = items.map(item => 'tiny/' + item + '.svg');
var icons;
Promise.all(urls.map(url => fetch(url).then(res => res.text()))).then(all => {
  icons = all;
  render(range.value);
});

var render = function(radius = 15){
  console.log('Rendering!', icons);

  icons = icons.map(icon => {
    return icon.replace(/rx\=\"\d{0,2}\%/, 'rx="' + radius + '%"');
  });
  container.innerHTML = '<div>' + icons.join('</div><div>') + '</div>';
}
