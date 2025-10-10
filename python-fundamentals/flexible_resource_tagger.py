def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates are ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.

    Raises:
        TypeError: If existing_tags is not a dictionary.
    """
    # TODO: Add validation here.
    # Check if 'existing_tags' is a dictionary.
    # If it's not, raise a TypeError with a helpful message.

    if not isinstance(existing_tags,dict):
        raise TypeError("must be a dictionary")
        
    ans=existing_tags.copy()
    key_new_tags= dict(key_value_tags)
    new_tags= list(set(simple_tags) - set(existing_tags.keys()))
    
    for tag in new_tags:
        ans[tag]='true'
    
    for key in key_new_tags:
        ans[key]= key_new_tags[key]
        
    
    return ans
