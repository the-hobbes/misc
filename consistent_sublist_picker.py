def ShardList(list_to_shard, total_shards, shard_idx):
  """Return a sublist of elements based on total shards desired and the shard index.

  ShardModules breaks the list of alert modules into total_shards sublists,
  then returns the sublist corresponding to the shard. Use this to split a
  list into an equal number of parts which are consistent each time the
  function is called.

  Args:
    list_to_shard (list): the list of elements to be sharded.
    total_shards (int): the total number of possible shards.
    shard_idx (int): the config shard these elements should be selected for.

  Returns:
    split_lists (list): the sublist of alert modules that should be installed
    for the provided config shard.
  """
  length = len(list_to_shard)
  split_lists = []
  for i in range(total_shards):
    start_idx = i * length // total_shards
    end_idx = (i + 1) * length // total_shards
    split_lists.append(list_to_shard[start_idx: end_idx])

  return split_lists[shard_idx]
