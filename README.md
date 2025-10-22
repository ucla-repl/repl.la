The most important part of a website is its content.
Therefore, the design of this website makes it as easy
 to keep up-to-date as possible.
Most problems during updates come from broken dependencies,
 so we only introduce a dependency if it's absolutely necessary.
Currently the only dependency is pandoc which is used
 by nearly all site generators, maintained by a healthy community,
 and will likely survive to the forseeable future.
In the same spirit, if something is simple enough to do manually
 we avoid brittle automated pipelines.
For example, we could have used a CI workflow to build the html from markdown,
 but we stick to typing `make` manually because that will always work
 and requires zero maintenance.
Also, we opt to manually update the RSS feed despite there being
 scripts that can generate feeds,
 so that we can directly fix the feed itself in case of errors
 instead of trying to debug the program generating the feed.
