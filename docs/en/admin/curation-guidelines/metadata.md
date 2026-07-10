---
title: Metadata
---

# Metadata

Select the Metadata tab, and click the Add + Edit Metadata button.

Curation checklist for the most common metadata fields (for a more detailed and extensive overview, see the Word document "Dataverse_North_metadata_best_practices_guide_v2.0_ENG.docx" in the Metadata og dokumentasjon channel in the DvNO-brukarforum Team):

- **Related publication:** If the dataset is the basis for a publication, is the reference to the publication provided here? If the dataset is used in a article or book manuscript that is submitted for review, but has not been accepted (yet), the name of the journal or publisher should not be mentioned in any place in the dataset. Rather, one should use the expression "Submitted for review" or the like. Also check with the researcher whether the article or book manuscript will be subject to double-blind review (both author and reviewers are anonymous) and the editor has asked for the dataset draft being available in anonymized form for this process. In that case, the curator creates an anonymized version of the dataset draft following the guidance on this page.

- **Language:** The field Language is not about the investigated language, but about the language of analyses. In a TROLLing dataset about French nouns described/analysed in English, this field should not contain "French", but "English" or be left empty. However, "French" should be added as a keyword.

- **Producer:** Has there been entered a correct Producer of the dataset? In institutional collection, this field is pre-populated. But in special collections of the TROLLing type, you should check whether the user has filled in the right institution (e.g. UiT The Arctic University of Norway or the name of another institution of funder). If the author is not associated with any research organization anymore, the name of the author may be added in inverted order to the Name-field, and the other fields may be left empty. For datasets which are deposited by bachelor or master students, there are two alternatives: a) If the student was employed or paid in any other way by a (research) organization to produce the deposited data, the name of the organization is added to the Name-field. b) If the student was not employed/paid to produce the dataset, the name of the student may be added in inverted order to the Name-field. If – still in case b – the dataset was produced while the student was studying at a HE institution, the name of the institution may be added to the Affiliation-field.

- **Contributor:** Here credit should be given to those who have contributed to the dataset, including those who are listed as authors. The role of the contributors can be defined in the Type field (e.g. Data Collector).

- **Grant Information:** If there are things indicating that the deposited data are from a project with external funding, the curator should ask the depositor about this, and ask him/her to fill in this field if applicable. Use the full name of the funder, e.g. "The Research Council of Norway".

- **Time Period Covered:** What time period is the data from or about?

- **Date of Collection:** When was the data collected / generated?

- **Data Type:** What type of data is it? For suggestions, the depositor may hover the mouse over the question mark to the right of the field name, e.g. survey data, experimental data, observation data.

- **Data Sources:** If the deposited data were not generated or collected by the depositor/research project, information should be entered here about the sources. This can for example be an archive, a corpus, or a website from which the data were downloaded. In addition, the Terms of Use / license(s) that apply for the used sources should be specified in this field.

- **Distributor:** As a rule, this field is pre-filled with the English name of the partner institution (e.g., UiT The Arctic University of Norway). Make sure the content has not been edited.

- **Geographic Coverage:** Many datasets are related to one or more geographical places or areas. In case the user has not entered any metadata about this in the metadata section Geospatial Metadata, you should recommend him/her to do so. In addition, you may ask the depositor to have a look at the domain-specific metadata schemas following Geospatial Metadata, and add relevant information if applicable.

**Generally:**

- Are the provided metadata sufficient to make the dataset findable in search engines?
- Are the metadata provided in English or another commonly used communication language in the scientific field in question?
- Note! Metadata fields must not contain certain HTML tags or other special characters (e.g. [ and ]). This applies in particular to the Description field. To add breaks between to sections, add the HTML tags `<p>` and `</p>` around each section.
- Are the fields filled in correctly? E.g.:
    - **Title:** Quotation marks should not be added around the title as such marks will be added automatically in the reference generated by the system. If the dataset contains background / replication data for a publication, "Replication data for: " may be added to the title of the dataset. Instead of "Replication Data for: " you may use "Background Data for: ", "Supporting Data for: " or another suitable suffix.
    - **Author:** Is/are the name(s) of the author(s) inverted (family name, given name)? Is affiliation provided (e.g. UiT The Arctic University of Norway)? Authors should be encouraged to create an ORCID, and add it to the Identifier Scheme field, e.g., 0000-0001-0003-0004 (without "https://orcid.org/").
    - **Contact:** If the contact is one or several persons, the name(s) have to be inverted (family name, given name). If the contact is an institution, the name is not inverted. Are affiliation and correct email address provided?
    - **Description:** A brief presentation of the dataset should be given. To add breaks between to sections, add the HTML tags `<p>` and `</p>` around each section. This description should usually also be included in the ReadMe file. One may use (parts of) the abstract of the related publication, in which case the abstract should be entered into a second description field, which can be added by clicking the plus button to the right. NB! If your article is only submitted and not accepted (yet), DO NOT mention the name of the journal it has been submitted to. The Date field must be filled in in the format YYYY-MM-DD.
    - **Keyword:** Are there reasonable keyword terms added? If there are more commonly used keywords already applied in the (sub)archive, you should make the user aware of this. Has each keyword been assigned its own field? If not, ask the user to replicate the field for each keyword.
