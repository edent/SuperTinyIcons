var items = [
  'amazon', 'phone', 'spotify', 'wechat', 'dropbox', 'instagram', 'hackernews',
  'pinterest', 'stackoverflow', 'whatsapp', 'email', 'linkedin', 'reddit',
  'steam', 'wikipedia', 'facebook', 'lock', 'rss', 'slideshare', 'telegram',
  'mail', 'skype', 'tumblr', 'wordpress', 'github', 'pdf', 'vk', 'wire',
  'twitter', 'youtube', 'google_plus', 'paypal', 'snapchat', 'vimeo', 'flickr',
  'soundcloud', 'html5', 'mastodon'
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

var urls = items.map(item => '/tiny/' + item + '.svg');
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
