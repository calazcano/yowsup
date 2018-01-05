# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
  name='wa.proto',
  package='com.whatsapp.proto',
  serialized_pb=_b('\n\x08wa.proto\x12\x12\x63om.whatsapp.proto\"\x95\x04\n\x07Message\x12\x14\n\x0c\x63onversation\x18\x01 \x01(\t\x12Y\n\x1fsender_key_distribution_message\x18\x02 \x01(\x0b\x32\x30.com.whatsapp.proto.SenderKeyDistributionMessage\x12\x37\n\rimage_message\x18\x03 \x01(\x0b\x32 .com.whatsapp.proto.ImageMessage\x12;\n\x0f\x63ontact_message\x18\x04 \x01(\x0b\x32\".com.whatsapp.proto.ContactMessage\x12=\n\x10location_message\x18\x05 \x01(\x0b\x32#.com.whatsapp.proto.LocationMessage\x12=\n\x10\x64ocument_message\x18\x07 \x01(\x0b\x32#.com.whatsapp.proto.DocumentMessage\x12\x33\n\x0burl_message\x18\x06 \x01(\x0b\x32\x1e.com.whatsapp.proto.UrlMessage\x12\x37\n\raudio_message\x18\x08 \x01(\x0b\x32 .com.whatsapp.proto.AudioMessage\x12\x37\n\rvideo_message\x18\t \x01(\x0b\x32 .com.whatsapp.proto.VideoMessage\"`\n\x1cSenderKeyDistributionMessage\x12\x0f\n\x07groupId\x18\x01 \x02(\t\x12/\n\'axolotl_sender_key_distribution_message\x18\x02 \x02(\x0c\"\xb3\x01\n\x0cImageMessage\x12\x0b\n\x03url\x18\x01 \x02(\x0c\x12\x11\n\tmime_type\x18\x02 \x02(\t\x12\x0f\n\x07\x63\x61ption\x18\x03 \x02(\t\x12\x13\n\x0b\x66ile_sha256\x18\x04 \x02(\x0c\x12\x13\n\x0b\x66ile_length\x18\x05 \x02(\x04\x12\x0e\n\x06height\x18\x06 \x02(\r\x12\r\n\x05width\x18\x07 \x02(\r\x12\x11\n\tmedia_key\x18\x08 \x02(\x0c\x12\x16\n\x0ejpeg_thumbnail\x18\x10 \x02(\x0c\"\xa6\x01\n\x0cVideoMessage\x12\x0b\n\x03url\x18\x01 \x02(\x0c\x12\x11\n\tmime_type\x18\x02 \x02(\t\x12\x13\n\x0b\x66ile_sha256\x18\x03 \x02(\x0c\x12\x13\n\x0b\x66ile_length\x18\x04 \x02(\x04\x12\x10\n\x08\x64uration\x18\x05 \x02(\x04\x12\x11\n\tmedia_key\x18\x06 \x02(\x0c\x12\x0f\n\x07\x63\x61ption\x18\x07 \x02(\t\x12\x16\n\x0ejpeg_thumbnail\x18\x10 \x02(\x0c\"\x8a\x01\n\x0c\x41udioMessage\x12\x0b\n\x03url\x18\x01 \x02(\x0c\x12\x11\n\tmime_type\x18\x02 \x02(\t\x12\x13\n\x0b\x66ile_sha256\x18\x03 \x02(\x0c\x12\x13\n\x0b\x66ile_length\x18\x04 \x02(\x04\x12\x10\n\x08\x64uration\x18\x05 \x02(\x04\x12\x0b\n\x03unk\x18\x06 \x02(\r\x12\x11\n\tmedia_key\x18\x07 \x02(\x0c\"\x8a\x01\n\x0fLocationMessage\x12\x18\n\x10\x64\x65grees_latitude\x18\x01 \x02(\x01\x12\x19\n\x11\x64\x65grees_longitude\x18\x02 \x02(\x01\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x02(\t\x12\x0b\n\x03url\x18\x05 \x02(\t\x12\x16\n\x0ejpeg_thumbnail\x18\x10 \x02(\x0c\"\xa9\x01\n\x0f\x44ocumentMessage\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x11\n\tmime_type\x18\x02 \x02(\t\x12\r\n\x05title\x18\x03 \x02(\t\x12\x13\n\x0b\x66ile_sha256\x18\x04 \x02(\x0c\x12\x13\n\x0b\x66ile_length\x18\x05 \x02(\x04\x12\x12\n\npage_count\x18\x06 \x02(\r\x12\x11\n\tmedia_key\x18\x07 \x02(\x0c\x12\x16\n\x0ejpeg_thumbnail\x18\x10 \x02(\x0c\"\x83\x01\n\nUrlMessage\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\x14\n\x0cmatched_text\x18\x02 \x02(\t\x12\x15\n\rcanonical_url\x18\x04 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x02(\t\x12\r\n\x05title\x18\x06 \x02(\t\x12\x16\n\x0ejpeg_thumbnail\x18\x10 \x02(\x0c\"5\n\x0e\x43ontactMessage\x12\x14\n\x0c\x64isplay_name\x18\x01 \x02(\t\x12\r\n\x05vcard\x18\x10 \x02(\x0c'))

_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='com.whatsapp.proto.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversation', full_name='com.whatsapp.proto.Message.conversation', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_key_distribution_message', full_name='com.whatsapp.proto.Message.sender_key_distribution_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_message', full_name='com.whatsapp.proto.Message.image_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contact_message', full_name='com.whatsapp.proto.Message.contact_message', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_message', full_name='com.whatsapp.proto.Message.location_message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='document_message', full_name='com.whatsapp.proto.Message.document_message', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_message', full_name='com.whatsapp.proto.Message.url_message', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_message', full_name='com.whatsapp.proto.Message.audio_message', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_message', full_name='com.whatsapp.proto.Message.video_message', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=566,
)


_SENDERKEYDISTRIBUTIONMESSAGE = _descriptor.Descriptor(
  name='SenderKeyDistributionMessage',
  full_name='com.whatsapp.proto.SenderKeyDistributionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='com.whatsapp.proto.SenderKeyDistributionMessage.groupId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axolotl_sender_key_distribution_message', full_name='com.whatsapp.proto.SenderKeyDistributionMessage.axolotl_sender_key_distribution_message', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=568,
  serialized_end=664,
)


_IMAGEMESSAGE = _descriptor.Descriptor(
  name='ImageMessage',
  full_name='com.whatsapp.proto.ImageMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='com.whatsapp.proto.ImageMessage.url', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='com.whatsapp.proto.ImageMessage.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='com.whatsapp.proto.ImageMessage.caption', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_sha256', full_name='com.whatsapp.proto.ImageMessage.file_sha256', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_length', full_name='com.whatsapp.proto.ImageMessage.file_length', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='com.whatsapp.proto.ImageMessage.height', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='com.whatsapp.proto.ImageMessage.width', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_key', full_name='com.whatsapp.proto.ImageMessage.media_key', index=7,
      number=8, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
#    _descriptor.FieldDescriptor(
#      name='file_enc_sha256', full_name='com.whatsapp.proto.ImageMessage.file_enc_sha256', index=8,
#      number=9, type=12, cpp_type=9, label=2,
#      has_default_value=False, default_value=_b(""),
#      message_type=None, enum_type=None, containing_type=None,
#      is_extension=False, extension_scope=None,
#      options=None),
    _descriptor.FieldDescriptor(
      name='jpeg_thumbnail', full_name='com.whatsapp.proto.ImageMessage.jpeg_thumbnail', index=9,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=667,
  serialized_end=846,
)


_VIDEOMESSAGE = _descriptor.Descriptor(
  name='VideoMessage',
  full_name='com.whatsapp.proto.VideoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='com.whatsapp.proto.VideoMessage.url', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='com.whatsapp.proto.VideoMessage.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_sha256', full_name='com.whatsapp.proto.VideoMessage.file_sha256', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_length', full_name='com.whatsapp.proto.VideoMessage.file_length', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='com.whatsapp.proto.VideoMessage.duration', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_key', full_name='com.whatsapp.proto.VideoMessage.media_key', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='com.whatsapp.proto.VideoMessage.caption', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    #_descriptor.FieldDescriptor(
    #  name='file_enc_sha256', full_name='com.whatsapp.proto.VideoMessage.file_enc_sha256', index=7,
    #  number=8, type=12, cpp_type=9, label=2,
    #  has_default_value=False, default_value=_b(""),
    #  message_type=None, enum_type=None, containing_type=None,
    #  is_extension=False, extension_scope=None,
    #  options=None),
    _descriptor.FieldDescriptor(
      name='jpeg_thumbnail', full_name='com.whatsapp.proto.VideoMessage.jpeg_thumbnail', index=8,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=849,
  serialized_end=1015,
)


_AUDIOMESSAGE = _descriptor.Descriptor(
  name='AudioMessage',
  full_name='com.whatsapp.proto.AudioMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='com.whatsapp.proto.AudioMessage.url', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='com.whatsapp.proto.AudioMessage.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_sha256', full_name='com.whatsapp.proto.AudioMessage.file_sha256', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_length', full_name='com.whatsapp.proto.AudioMessage.file_length', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='com.whatsapp.proto.AudioMessage.duration', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unk', full_name='com.whatsapp.proto.AudioMessage.unk', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_key', full_name='com.whatsapp.proto.AudioMessage.media_key', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1018,
  serialized_end=1156,
)


_LOCATIONMESSAGE = _descriptor.Descriptor(
  name='LocationMessage',
  full_name='com.whatsapp.proto.LocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='degrees_latitude', full_name='com.whatsapp.proto.LocationMessage.degrees_latitude', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='degrees_longitude', full_name='com.whatsapp.proto.LocationMessage.degrees_longitude', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.whatsapp.proto.LocationMessage.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='com.whatsapp.proto.LocationMessage.address', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='com.whatsapp.proto.LocationMessage.url', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jpeg_thumbnail', full_name='com.whatsapp.proto.LocationMessage.jpeg_thumbnail', index=3,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1159,
  serialized_end=1297,
)


_DOCUMENTMESSAGE = _descriptor.Descriptor(
  name='DocumentMessage',
  full_name='com.whatsapp.proto.DocumentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='com.whatsapp.proto.DocumentMessage.url', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='com.whatsapp.proto.DocumentMessage.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='com.whatsapp.proto.DocumentMessage.title', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_sha256', full_name='com.whatsapp.proto.DocumentMessage.file_sha256', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_length', full_name='com.whatsapp.proto.DocumentMessage.file_length', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_count', full_name='com.whatsapp.proto.DocumentMessage.page_count', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_key', full_name='com.whatsapp.proto.DocumentMessage.media_key', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jpeg_thumbnail', full_name='com.whatsapp.proto.DocumentMessage.jpeg_thumbnail', index=7,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1300,
  serialized_end=1469,
)


_URLMESSAGE = _descriptor.Descriptor(
  name='UrlMessage',
  full_name='com.whatsapp.proto.UrlMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='com.whatsapp.proto.UrlMessage.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matched_text', full_name='com.whatsapp.proto.UrlMessage.matched_text', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='canonical_url', full_name='com.whatsapp.proto.UrlMessage.canonical_url', index=2,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='com.whatsapp.proto.UrlMessage.description', index=3,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='com.whatsapp.proto.UrlMessage.title', index=4,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jpeg_thumbnail', full_name='com.whatsapp.proto.UrlMessage.jpeg_thumbnail', index=5,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1472,
  serialized_end=1603,
)


_CONTACTMESSAGE = _descriptor.Descriptor(
  name='ContactMessage',
  full_name='com.whatsapp.proto.ContactMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='com.whatsapp.proto.ContactMessage.display_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vcard', full_name='com.whatsapp.proto.ContactMessage.vcard', index=1,
      number=16, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1605,
  serialized_end=1658,
)

_MESSAGE.fields_by_name['sender_key_distribution_message'].message_type = _SENDERKEYDISTRIBUTIONMESSAGE
_MESSAGE.fields_by_name['image_message'].message_type = _IMAGEMESSAGE
_MESSAGE.fields_by_name['contact_message'].message_type = _CONTACTMESSAGE
_MESSAGE.fields_by_name['location_message'].message_type = _LOCATIONMESSAGE
_MESSAGE.fields_by_name['document_message'].message_type = _DOCUMENTMESSAGE
_MESSAGE.fields_by_name['url_message'].message_type = _URLMESSAGE
_MESSAGE.fields_by_name['audio_message'].message_type = _AUDIOMESSAGE
_MESSAGE.fields_by_name['video_message'].message_type = _VIDEOMESSAGE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['SenderKeyDistributionMessage'] = _SENDERKEYDISTRIBUTIONMESSAGE
DESCRIPTOR.message_types_by_name['ImageMessage'] = _IMAGEMESSAGE
DESCRIPTOR.message_types_by_name['VideoMessage'] = _VIDEOMESSAGE
DESCRIPTOR.message_types_by_name['AudioMessage'] = _AUDIOMESSAGE
DESCRIPTOR.message_types_by_name['LocationMessage'] = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['DocumentMessage'] = _DOCUMENTMESSAGE
DESCRIPTOR.message_types_by_name['UrlMessage'] = _URLMESSAGE
DESCRIPTOR.message_types_by_name['ContactMessage'] = _CONTACTMESSAGE


Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.Message)
  ))
_sym_db.RegisterMessage(Message)

SenderKeyDistributionMessage = _reflection.GeneratedProtocolMessageType('SenderKeyDistributionMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENDERKEYDISTRIBUTIONMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.SenderKeyDistributionMessage)
  ))
_sym_db.RegisterMessage(SenderKeyDistributionMessage)

ImageMessage = _reflection.GeneratedProtocolMessageType('ImageMessage', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.ImageMessage)
  ))
_sym_db.RegisterMessage(ImageMessage)

AudioMessage = _reflection.GeneratedProtocolMessageType('AudioMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.VideoMessage)
  ))
_sym_db.RegisterMessage(AudioMessage)

VideoMessage = _reflection.GeneratedProtocolMessageType('VideoMessage', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.VideoMessage)
  ))
_sym_db.RegisterMessage(VideoMessage)

LocationMessage = _reflection.GeneratedProtocolMessageType('LocationMessage', (_message.Message,), dict(
  DESCRIPTOR = _LOCATIONMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.LocationMessage)
  ))
_sym_db.RegisterMessage(LocationMessage)

DocumentMessage = _reflection.GeneratedProtocolMessageType('DocumentMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.DocumentMessage)
  ))
_sym_db.RegisterMessage(DocumentMessage)

UrlMessage = _reflection.GeneratedProtocolMessageType('UrlMessage', (_message.Message,), dict(
  DESCRIPTOR = _URLMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.UrlMessage)
  ))
_sym_db.RegisterMessage(UrlMessage)

ContactMessage = _reflection.GeneratedProtocolMessageType('ContactMessage', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTMESSAGE,
  __module__ = 'wa_pb2'
  # @@protoc_insertion_point(class_scope:com.whatsapp.proto.ContactMessage)
  ))
_sym_db.RegisterMessage(ContactMessage)


# @@protoc_insertion_point(module_scope)