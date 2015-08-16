# -*- coding: UTF-8 -*-

from portality.lib import dataobj
from portality import models
from portality.formcontext import choices
from copy import deepcopy

class IncomingApplication(dataobj.DataObj):
    def __init__(self, raw=None):
        struct = {
            "fields": {
                "id": {"coerce": "unicode"},                # Note that we'll leave these in for ease of use by the
                "created_date": {"coerce": "utcdatetime"},  # caller, but we'll need to ignore them on the conversion
                "last_updated": {"coerce": "utcdatetime"}   # to the real object
            },
            "objects": ["bibjson", "suggestion", "admin"],
            "required" : ["bibjson", "suggestion", "admin"],

            "structs": {
                "bibjson": {
                    "fields": {
                        "allows_fulltext_indexing": {"coerce": "bool"},
                        "alternative_title": {"coerce": "unicode"},
                        "apc_url": {"coerce": "url"},
                        "country": {"coerce": "country_code"},
                        "institution": {"coerce": "unicode"},
                        "provider": {"coerce": "unicode"},
                        "publication_time": {"coerce": "integer"},
                        "publisher": {"coerce": "unicode"},
                        "submission_charges_url": {"coerce": "url"},
                        "title": {"coerce": "unicode"},
                    },
                    "lists": {
                        "deposit_policy": {"coerce": "deposit_policy", "contains": "field"},
                        "format": {"coerce": "format", "contains": "field"},
                        "identifier": {"contains": "object"},
                        "keywords": {"coerce": "unicode", "contains": "field"},
                        "language": {"coerce": "isolang_2letter", "contains": "field"},
                        "license": {"contains": "object"},
                        "link": {"contains": "object"},
                        "persistent_identifier_scheme": {"coerce": "persistent_identifier_scheme", "contains": "field"},
                    },
                    "objects": [
                        "apc",
                        "archiving_policy",
                        "article_statistics",
                        "author_copyright",
                        "author_publishing_rights",
                        "editorial_review",
                        "oa_start",
                        "plagiarism_detection",
                        "submission_charges",
                    ],
                    "required": [
                        "title",
                        "publisher",
                        "country",
                        "apc_url",
                        "submission_charges_url",
                        "allows_fulltext_indexing",
                        "publication_time",
                        "identifier",
                        "keywords",
                        "language",
                        "link",
                        "deposit_policy",
                        "persistent_identifier_scheme",
                        "format",
                        "license",
                        "oa_start",
                        "archiving_policy",
                        "editorial_review",
                        "plagiarism_detection",
                        "article_statistics",
                        "author_copyright",
                        "author_publishing_rights"
                    ],


                    "structs": {
                        "oa_start": {
                            "fields": {
                                "year": {"coerce": "integer"}
                            },
                            "required" : ["year"]
                        },

                        "apc": {
                            "fields": {
                                "currency": {"coerce": "currency_code"},
                                "average_price": {"coerce": "integer"}
                            }
                        },

                        "submission_charges": {
                            "fields": {
                                "currency": {"coerce": "currency_code"},
                                "average_price": {"coerce": "integer"}
                            }
                        },

                        "archiving_policy": {               # NOTE: this is not the same as the storage model, so beware when working with this
                            "fields": {
                                "url": {"coerce": "url"},
                            },
                            "lists": {
                                "policy": {"coerce": "unicode", "contains": "object"},
                            },
                            "required" : ["url", "policy"],

                            "structs" : {
                                "policy" : {
                                    "fields" : {
                                        "name" : {"coerce": "unicode"},
                                        "domain" : {"coerce" : "unicode"}
                                    },
                                    "required" : ["name"]
                                }
                            }
                        },

                        "editorial_review": {
                            "fields": {
                                "process": {"coerce": "unicode", "allowed_values" : ["Editorial review", "Peer review", "Blind peer review", "Double blind peer review", "Open peer review", "None"]},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["process", "url"]
                        },

                        "plagiarism_detection": {
                            "fields": {
                                "detection": {"coerce": "bool"},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["detection", "url"]
                        },

                        "article_statistics": {
                            "fields": {
                                "statistics": {"coerce": "bool"},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["statistics"]
                        },

                        "author_copyright": {
                            "fields": {
                                "copyright": {"coerce": "unicode"},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["copyright"]
                        },

                        "author_publishing_rights": {
                            "fields": {
                                "publishing_rights": {"coerce": "unicode"},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["publishing_rights"]
                        },

                        "identifier": {
                            "fields": {
                                "type": {"coerce": "unicode"},
                                "id": {"coerce": "unicode"},
                            },
                            "required" : ["type", "id"]
                        },

                        "link": {
                            "fields": {
                                "type": {"coerce": "unicode"},
                                "url": {"coerce": "url"},
                            },
                            "required" : ["type", "url"]
                        },

                        "license": {
                            "fields": {
                                "title": {"coerce": "license"},
                                "type": {"coerce": "license"},
                                "url": {"coerce": "unicode"},
                                "version": {"coerce": "unicode"},
                                "open_access": {"coerce": "bool"},
                                "BY": {"coerce": "bool"},
                                "NC": {"coerce": "bool"},
                                "ND": {"coerce": "bool"},
                                "SA": {"coerce": "bool"},
                                "embedded": {"coerce": "bool"},
                                "embedded_example_url": {"coerce": "url"},
                            },
                            "required" : [
                                "embedded",
                                "title",
                                "type",
                                "open_access"
                            ]
                        }
                    }
                },

                "suggestion" : {
                    "fields" : {
                        "article_metadata" : {"coerce" : "bool"}
                    },
                    "objects" : [
                        "articles_last_year"
                    ],
                    "required" : ["article_metadata", "articles_last_year"],

                    "structs" : {
                        "articles_last_year" : {
                            "fields" : {
                                "count" : {"coerce" : "integer"},
                                "url" : {"coerce" : "url"}
                            },
                            "required" : ["count", "url"]
                        }
                    }
                },

                "admin" : {
                    "lists" : {
                        "contact" : {"contains" : "object"}
                    },
                    "required" : ["contact"],

                    "structs" : {
                        "contact": {
                            "fields" : {
                                "email" : {"coerce" : "unicode"},
                                "name" : {"coerce" : "unicode"}
                            },
                            "required" : ["name", "email"]
                        }
                    }
                }
            }
        }

        mycoerce = deepcopy(self.DEFAULT_COERCE)
        mycoerce["persistent_identifier_scheme"] = dataobj.string_canonicalise(["None", "DOI", "Handles", "ARK"], allow_fail=True)
        mycoerce["format"] = dataobj.string_canonicalise(["PDF", "HTML", "ePUB", "XML"], allow_fail=True)
        mycoerce["license"] = dataobj.string_canonicalise(["CC BY", "CC BY-NC", "CC BY-NC-ND", "CC BY-NC-SA", "CC BY-ND", "CC BY-SA", "Not CC-like"], allow_fail=True)
        mycoerce["deposit_policy"] = dataobj.string_canonicalise(["None", "Sherpa/Romeo", "Dulcinea", "OAKlist", "Héloïse", "Diadorim"], allow_fail=True)

        super(IncomingApplication, self).__init__(raw, struct=struct, construct_silent_prune=False, expose_data=True, coerce_map=mycoerce)

    def custom_validate(self):
        # only attempt to validate if this is not a blank object
        if len(self.data.keys()) == 0:
            return

        # at least one of print issn / e-issn, and they must be different
        #
        # check that there are identifiers at all
        identifiers = self.bibjson.identifier
        if identifiers is None or len(identifiers) == 0:
            raise dataobj.DataStructureException("You must specify at least one of P-ISSN or E-ISSN in bibjson.identifier")

        # extract the p/e-issn identifier objects
        pissn = None
        eissn = None
        for ident in identifiers:
            if ident.type == "pissn":
                pissn = ident
            elif ident.type == "eissn":
                eissn = ident

        # check that at least one of them appears
        if pissn is None and eissn is None:
            raise dataobj.DataStructureException("You must specify at least one of P-ISSN or E-ISSN in bibjson.identifier")

        # normalise the ids
        pissn.id = self._normalise_issn(pissn.id)
        eissn.id = self._normalise_issn(eissn.id)

        # check they are not the same
        if pissn.id == eissn.id:
            raise dataobj.DataStructureException("P-ISSN and E-ISSN should be different")

        # A link to the journal homepage is required
        #
        # check that there are links at all
        links = self.bibjson.link
        if links is None or len(links) == 0:
            raise dataobj.DataStructureException("You must specify the journal homepage in bibjson.link@type='homepage'")
        found = False
        for l in links:
            if l.type == "homepage":
                found = True
                break
        if not found:
            raise dataobj.DataStructureException("You must specify the journal homepage in bibjson.link@type='homepage'")

        # if plagiarism detection is done, then the url is a required field
        if self.bibjson.plagiarism_detection.detection is True:
            url = self.bibjson.plagiarism_detection.url
            if url is None:
                raise dataobj.DataStructureException("In this context bibjson.plagiarism_detection.url is required")

        # if licence.embedded is true, then the url is a required field
        lic = self.bibjson.license
        if lic is not None and len(lic) > 0:
            lic = lic[0]
            if lic.embedded:
                if lic.embedded_example_url is None:
                    raise dataobj.DataStructureException("In this context bibjson.license.embedded_example_url is required")

        # if the author does not hold the copyright the url is optional, otherwise it is required
        if self.bibjson.author_copyright.copyright is not False:
            if self.bibjson.author_copyright.url is None:
                raise dataobj.DataStructureException("In this context bibjson.author_copyright.url is required")

        # if the author does not hold the publishing rights the url is optional, otherwise it is required
        if self.bibjson.author_publishing_rights.publishing_rights is not False:
            if self.bibjson.author_publishing_rights.url is None:
                raise dataobj.DataStructureException("In this context bibjson.author_copyright.url is required")

        # if the archiving policy has no "domain" set, then the policy must be from one of an allowed list
        # if the archiving policy does have "domain" set, then the domain must be from one of an allowed list
        for ap in self.bibjson.archiving_policy.policy:
            if ap.domain is not None:
                # domain is in allowed list
                opts = choices.Choices.digital_archiving_policy_list("optional")
                if ap.domain not in opts:
                    raise dataobj.DataStructureException("bibjson.archiving_policy.policy.domain must be one of {x}".format(x=" or ".join(opts)))
            else:
                # policy name is in allowed list
                opts = choices.Choices.digital_archiving_policy_list("named")
                if ap.name not in opts:
                    raise dataobj.DataStructureException("bibjson.archiving_policy.policy.name must be one of '{x}' when 'domain' is not also set".format(x=", ".join(opts)))

        # check the number of keywords is no more than 6
        if len(self.bibjson.keywords) > 6:
            raise dataobj.DataStructureException("bibjson.keywords may only contain a maximum of 6 keywords")

    def _normalise_issn(self, issn):
        issn = issn.upper()
        if len(issn) > 8: return issn
        if len(issn) == 8:
            if "-" in issn: return "0" + issn
            else: return issn[:4] + "-" + issn[4:]
        if len(issn) < 8:
            if "-" in issn: return ("0" * (9 - len(issn))) + issn
            else:
                issn = ("0" * (8 - len(issn))) + issn
                return issn[:4] + "-" + issn[4:]

    def to_application_model(self):
        nd = deepcopy(self.data)

        # we need to re-write the archiving policy section
        ap = nd.get("bibjson", {}).get("archiving_policy")
        if ap is not None:
            nap = {}
            if "url" in ap:
                nap["url"] = ap["url"]
            if "policy" in ap:
                npol = []
                for pol in ap["policy"]:
                    if "domain" in pol:
                        npol.append([pol.get("domain"), pol.get("name")])
                    else:
                        npol.append(pol.get("name"))
                nap["policy"] = npol
            nd["bibjson"]["archiving_policy"] = nap

        return models.Suggestion(**nd)

    """
    @classmethod
    def from_model(cls, jm):
        assert isinstance(jm, models.Suggestion)
        return cls(jm.data)

    @classmethod
    def from_model_by_id(cls, id_):
        j = models.Suggestion.pull(id_)
        return cls.from_model(j)
    """
