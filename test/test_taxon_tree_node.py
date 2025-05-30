# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mosquito_alert.models.taxon_tree_node import TaxonTreeNode

class TestTaxonTreeNode(unittest.TestCase):
    """TaxonTreeNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaxonTreeNode:
        """Test TaxonTreeNode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaxonTreeNode`
        """
        model = TaxonTreeNode()
        if include_optional:
            return TaxonTreeNode(
                id = 56,
                name = '',
                common_name = '',
                rank = 'class',
                italicize = True,
                is_relevant = True,
                children = [
                    mosquito_alert.models.taxon_tree_node.TaxonTreeNode(
                        id = 56, 
                        name = '', 
                        common_name = '', 
                        rank = 'class', 
                        italicize = True, 
                        is_relevant = True, 
                        children = [
                            mosquito_alert.models.taxon_tree_node.TaxonTreeNode(
                                id = 56, 
                                name = '', 
                                common_name = '', 
                                rank = 'class', 
                                italicize = True, 
                                is_relevant = True, 
                                children = [
                                    
                                    ], )
                            ], )
                    ]
            )
        else:
            return TaxonTreeNode(
                id = 56,
                name = '',
                rank = 'class',
                italicize = True,
                is_relevant = True,
                children = [
                    mosquito_alert.models.taxon_tree_node.TaxonTreeNode(
                        id = 56, 
                        name = '', 
                        common_name = '', 
                        rank = 'class', 
                        italicize = True, 
                        is_relevant = True, 
                        children = [
                            mosquito_alert.models.taxon_tree_node.TaxonTreeNode(
                                id = 56, 
                                name = '', 
                                common_name = '', 
                                rank = 'class', 
                                italicize = True, 
                                is_relevant = True, 
                                children = [
                                    
                                    ], )
                            ], )
                    ],
        )
        """

    def testTaxonTreeNode(self):
        """Test TaxonTreeNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
