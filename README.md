# Super Simple Template Language

The Super Simple Template Language tool wraps \<p\> tags around paragraphs.

## Usage

Call sstl like this:

python3 sstl.py <name_of_template>

The only keyword in an sstl template file is "START_BODY" followed by a newline. Everything before and including "START_BODY" is printed as is (for processing by another application, for instance), and everything afterwards is parsed as part of the template and printed as html.

## Motivation

I need a simple template language & html generator for my blog.

## Roadmap

 - Ability to encode metadata that is not parsed (for feeding into other tools)
 - \<a\> tags
 - \<code\> tags
