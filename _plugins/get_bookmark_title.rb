# A basic MetaInspector to get the title from a regular mf-bookmark-of URL
#
# Usage example in your template
# {{page.mf-bookmark-of[0] | get_bookmark_title}}
# - It needs the array-count for some reason...-
require 'metainspector'
module GetBookmarkTitle
  def get_bookmark_title( input )
    bookmark = MetaInspector.new(input);
    puts "#{bookmark.title}"
  end

  def get_bookmark_description (input)
    bookmark2 = MetaInspector.new(input);
    puts "#{bookmark2.description}"
  end
end
Liquid::Template.register_filter(GetBookmarkTitle)