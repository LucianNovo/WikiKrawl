��          �   %   �      p    q  *   �     �  ,   �  V   �  X   U  Q   �  '      m   (  F   �  �   �  i   g	  c   �	  V   5
  V   �
  j   �
  `   N  e   �  q     J   �  L   �  8     D   X  U   �  m   �  W   a  i   �  �  #    �  *   
     5  ,   U  V   �  X   �  Q   2  '   �  m   �  F     �   a  i   �  c   U  V   �  V     j   g  `   �  e   3  q   �  J     L   V  8   �  D   �  U   !  m   w  W   �  i   =                                                                            
   	                                            
We've all done it.  In the process of writing a brand new application we've
discovered that we need a little bit of code that we've invented before.
Perhaps it's something to handle unicode text.  Perhaps it's something to make
a bit of python-2.5 code run on python-2.3.  Whatever it is, it ends up being
a tiny bit of code that seems too small to worry about pushing into its own
module so it sits there, a part of your current project, waiting to be cut and
pasted into your next project.  And the next.  And the next.  And since that
little bittybit of code proved so useful to you, it's highly likely that it
proved useful to someone else as well.  Useful enough that they've written it
and copy and pasted it over and over into each of their new projects.

Well, no longer!  Kitchen aims to pull these small snippets of code into a few
python modules which you can import and use within your project.  No more copy
and paste!  Now you can let someone else maintain and release these small
snippets so that you can get on with your life.
 ASCII control code present in string input First argument must be callable Kitchen contains a cornucopia of useful code The control_chars argument to unicode_to_xml must be one of ignore, replace, or strict The strategy argument to process_control_chars must be one of ignore, replace, or strict _ucp_width does not understand how to assign a width value to control characters. byte_string must be a byte string (str) byte_string_to_xml can only take a byte string as its first argument.  Use unicode_to_xml for unicode strings html_entities_unescape must have a unicode type for its first argument kitchen.text.converters.to_utf8 is deprecated.  Use kitchen.text.converters.to_bytes(obj, encoding="utf-8", nonstring="passthru" instead. kitchen.text.converters.to_xml is deprecated.  Use kitchen.text.converters.guess_encoding_to_xml instead. kitchen.text.utf8._utf8_width_le is deprecated.  Use kitchen.text.display._textual_width_le instead kitchen.text.utf8.utf8_text_fill is deprecated.  Use kitchen.text.display.fill instead kitchen.text.utf8.utf8_text_wrap is deprecated.  Use kitchen.text.display.wrap instead kitchen.text.utf8.utf8_valid is deprecated.  Use kitchen.text.misc.byte_string_valid_encoding(msg) instead kitchen.text.utf8.utf8_width is deprecated.  Use kitchen.text.display.textual_width(msg) instead kitchen.text.utf8.utf8_width_chop is deprecated.  Use kitchen.text.display.textual_width_chop instead kitchen.text.utf8.utf8_width_fill is deprecated.  Use kitchen.text.display.byte_string_textual_width_fill instead non_string is a deprecated parameter of to_bytes().  Use nonstring instead non_string is a deprecated parameter of to_unicode().  Use nonstring instead nonstring value, %(param)s, is not set to a valid action process_control_char must have a unicode type as the first argument. to_bytes was given "%(obj)s" which is neither a unicode string or a byte string (str) to_str is deprecated.  Use to_unicode or to_bytes instead.  See the to_str docstring for porting information. to_unicode was given "%(obj)s" which is neither a byte string (str) or a unicode string unicode_to_xml must have a unicode type as the first argument.  Use bytes_string_to_xml for byte strings. Project-Id-Version: Kitchen: Miscellaneous, useful  python code
Report-Msgid-Bugs-To: https://fedorahosted.org/kitchen/
POT-Creation-Date: 2012-01-03 18:23-0800
PO-Revision-Date: 2012-01-03 07:48+0000
Last-Translator: Toshio Kuratomi <a.badger@gmail.com>
Language-Team: LANGUAGE <LL@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 0.9.6
Language: en_US
Plural-Forms: nplurals=2; plural=(n != 1)
 
We've all done it.  In the process of writing a brand new application we've
discovered that we need a little bit of code that we've invented before.
Perhaps it's something to handle unicode text.  Perhaps it's something to make
a bit of python-2.5 code run on python-2.3.  Whatever it is, it ends up being
a tiny bit of code that seems too small to worry about pushing into its own
module so it sits there, a part of your current project, waiting to be cut and
pasted into your next project.  And the next.  And the next.  And since that
little bittybit of code proved so useful to you, it's highly likely that it
proved useful to someone else as well.  Useful enough that they've written it
and copy and pasted it over and over into each of their new projects.

Well, no longer!  Kitchen aims to pull these small snippets of code into a few
python modules which you can import and use within your project.  No more copy
and paste!  Now you can let someone else maintain and release these small
snippets so that you can get on with your life.
 ASCII control code present in string input First argument must be callable Kitchen contains a cornucopia of useful code The control_chars argument to unicode_to_xml must be one of ignore, replace, or strict The strategy argument to process_control_chars must be one of ignore, replace, or strict _ucp_width does not understand how to assign a width value to control characters. byte_string must be a byte string (str) byte_string_to_xml can only take a byte string as its first argument.  Use unicode_to_xml for unicode strings html_entities_unescape must have a unicode type for its first argument kitchen.text.converters.to_utf8 is deprecated.  Use kitchen.text.converters.to_bytes(obj, encoding="utf-8", nonstring="passthru" instead. kitchen.text.converters.to_xml is deprecated.  Use kitchen.text.converters.guess_encoding_to_xml instead. kitchen.text.utf8._utf8_width_le is deprecated.  Use kitchen.text.display._textual_width_le instead kitchen.text.utf8.utf8_text_fill is deprecated.  Use kitchen.text.display.fill instead kitchen.text.utf8.utf8_text_wrap is deprecated.  Use kitchen.text.display.wrap instead kitchen.text.utf8.utf8_valid is deprecated.  Use kitchen.text.misc.byte_string_valid_encoding(msg) instead kitchen.text.utf8.utf8_width is deprecated.  Use kitchen.text.display.textual_width(msg) instead kitchen.text.utf8.utf8_width_chop is deprecated.  Use kitchen.text.display.textual_width_chop instead kitchen.text.utf8.utf8_width_fill is deprecated.  Use kitchen.text.display.byte_string_textual_width_fill instead non_string is a deprecated parameter of to_bytes().  Use nonstring instead non_string is a deprecated parameter of to_unicode().  Use nonstring instead nonstring value, %(param)s, is not set to a valid action process_control_char must have a unicode type as the first argument. to_bytes was given "%(obj)s" which is neither a unicode string or a byte string (str) to_str is deprecated.  Use to_unicode or to_bytes instead.  See the to_str docstring for porting information. to_unicode was given "%(obj)s" which is neither a byte string (str) or a unicode string unicode_to_xml must have a unicode type as the first argument.  Use bytes_string_to_xml for byte strings. 