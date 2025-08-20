import { feedPlugin } from "@11ty/eleventy-plugin-rss";

export default function (eleventyConfig) {
	eleventyConfig.ignores.add("**blog/drafts/**");

	eleventyConfig.addPlugin(feedPlugin, {
		type: "atom", // or "rss", "json"
		outputPath: "/blog/feed.xml",
		collection: {
			name: "post", // iterate over `collections.post`
			limit: 20,     // 0 means no limit
		},
		metadata: {
			language: "en",
			title: "River's Blog",
			subtitle: "A blog about whatever technical stuff I feel like talking about today",
			base: "https://rseeber.github.io/blog/",
			author: {
				name: "River Seeber",
				email: "riverseeber12@gmail.com", // Optional
			}
		}
	});
};

export const config = {
  dir: {
		output: "/home/river/code/web/rseeber2/docs/",
  }
};
