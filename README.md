# Read Me
<h4>This is my website to complete my study of python object-oriented programming with the Django framework. I created a news website to easily share the latest happenings and to know the working process of backend developers<h4>
<hr>
I started by creating a wireframe first using <a href="https://whimsical.com/embed/Dc7Xc6wdD59N4XNK21WvbS" target="blank">whimsical</a>. I divided it into 4 pages. The home page contains all the latest happening news from various categories. The category page contains all the latest news related to the selected category. The search page contains news related to the keywords used. Post page that contains detailed information related to the selected news
<br>
&emsp;Then due to time constraints, I created a website UI or slicing directly using a wireframe-based bootstrap framework. Once done, I created a Django project by building an app based on the main categories and creating a model for news posts.
When creating the URL for my website, I use the slug <i>[domain name]/[main category]/[subcategory if exists]/[news post title]<i> so that my website can run dynamically by setting on views to direct it to the appropriate category and news post.
