# SPDX-FileCopyrightText: Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import os

from nv_ingest.util.converters.formats import ingest_json_results_to_blob


sample_result_text_json = """
[
  {
    "document_type": "text",
    "metadata": {
      "chart_metadata": null,
      "content": "TestingDocument\r\nA sample document with headings and placeholder text\r\nIntroduction\r\nThis is a placeholder document that can be used for any purpose. It contains some \r\nheadings and some placeholder text to fill the space. The text is not important and contains \r\nno real value, but it is useful for testing. Below, we will have some simple tables and charts \r\nthat we can use to confirm Ingest is working as expected.\r\nTable 1\r\nThis table describes some animals, and some activities they might be doing in specific \r\nlocations.\r\nAnimal Activity Place\r\nGira@e Driving a car At the beach\r\nLion Putting on sunscreen At the park\r\nCat Jumping onto a laptop In a home o@ice\r\nDog Chasing a squirrel In the front yard\r\nChart 1\r\nThis chart shows some gadgets, and some very fictitious costs. Section One\r\nThis is the first section of the document. It has some more placeholder text to show how \r\nthe document looks like. The text is not meant to be meaningful or informative, but rather to \r\ndemonstrate the layout and formatting of the document.\r\n\u2022 This is the first bullet point\r\n\u2022 This is the second bullet point\r\n\u2022 This is the third bullet point\r\nSection Two\r\nThis is the second section of the document. It is more of the same as we\u2019ve seen in the rest \r\nof the document. The content is meaningless, but the intent is to create a very simple \r\nsmoke test to ensure extraction is working as intended. This will be used in CI as time goes \r\non to ensure that changes we make to the library do not negatively impact our accuracy.\r\nTable 2\r\nThis table shows some popular colors that cars might come in.\r\nCar Color1 Color2 Color3\r\nCoupe White Silver Flat Gray\r\nSedan White Metallic Gray Matte Gray\r\nMinivan Gray Beige Black\r\nTruck Dark Gray Titanium Gray Charcoal\r\nConvertible Light Gray Graphite Slate Gray\r\nPicture\r\nBelow, is a high-quality picture of some shapes. Chart 2\r\nThis chart shows some average frequency ranges for speaker drivers.\r\nConclusion\r\nThis is the conclusion of the document. It has some more placeholder text, but the most \r\nimportant thing is that this is the conclusion. As we end this document, we should have \r\nbeen able to extract 2 tables, 2 charts, and some text including 3 bullet points.",
      "content_metadata": {
        "description": "Unstructured text from PDF document.",
        "hierarchy": {
          "block": -1,
          "line": -1,
          "nearby_objects": {
            "images": {
              "bbox": [],
              "content": []
            },
            "structured": {
              "bbox": [],
              "content": []
            },
            "text": {
              "bbox": [],
              "content": []
            }
          },
          "page": -1,
          "page_count": 3,
          "span": -1
        },
        "page_number": -1,
        "subtype": "",
        "type": "text"
      },
      "content_url": "",
      "debug_metadata": null,
      "embedding": null,
      "error_metadata": null,
      "image_metadata": null,
      "info_message_metadata": null,
      "raise_on_failure": false,
      "source_metadata": {
        "access_level": 1,
        "collection_id": "",
        "date_created": "2025-01-16T21:31:28.929797",
        "last_modified": "2025-01-16T21:31:28.929648",
        "partition_id": -1,
        "source_id": "/home/jeremy/Development/nv-ingest/data/multimodal_test.pdf",
        "source_location": "",
        "source_name": "/home/jeremy/Development/nv-ingest/data/multimodal_test.pdf",
        "source_type": "PDF",
        "summary": ""
      },
      "table_metadata": null,
      "text_metadata": {
        "keywords": "",
        "language": "en",
        "summary": "",
        "text_location": [
          -1,
          -1,
          -1,
          -1
        ],
        "text_type": "document"
      }
    }
  }
]
"""  # noqa: E501


def test_json_results_to_blob_text_failure():
    # there must be a "data" element in the json otherwise empty is returned
    blob_response = ingest_json_results_to_blob(sample_result_text_json)
    assert blob_response == ""


def test_json_results_to_blob():
    current_directory = os.path.dirname(__file__)

    # Construct the full path to the target file
    file_name = "multimodal_test_raw_results.json"
    file_path = os.path.join(current_directory, file_name)

    with open(file_path, "r") as file:
        json_result_raw_data = json.load(file)
        blob_response = ingest_json_results_to_blob(json.dumps(json_result_raw_data))

        # The actual output is quite large. So we just check for key pieces being present
        assert "Tweeter - Midrange - Midwoofer - Subwoofer Hertz" in blob_response
