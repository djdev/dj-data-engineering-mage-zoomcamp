if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    print('Preprocessing: rows with zero passengers:', data['passenger_count'].isin([0]).sum())
    print('Preprocessing: rows with trip distance equal to zero:', data['trip_distance'].isin([0.00]).sum())
    # Specify your transformation logic here

    # filter out zero passenger trips
    data = data[data['passenger_count'] > 0]
    
    # filter out trip distance equal to zero
    data = data[data['trip_distance'] > 0.00]

    # create new column
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # rename columns with Camel Case to Snake Case
    data.columns = (data.columns
                        .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                        .str.lower()
                    )

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0.00]).sum() == 0, 'There are rides with where trip distance is zero'
