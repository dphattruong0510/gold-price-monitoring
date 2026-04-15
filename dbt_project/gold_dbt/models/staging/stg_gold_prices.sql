with parent as (

    select *
    from {{ source('gold_raw', 'prices') }}

),

child as (

    select *
    from {{ source('gold_raw', 'prices__entries') }}

),

joined as (

    select
        cast(parent.timestamp as timestamp) as price_timestamp,
        cast(parent.date as date) as price_date,
        child.brand as brand,
        cast(child.buy as numeric) as buy_price,
        cast(child.sell as numeric) as sell_price,
        parent._dlt_id as parent_dlt_id,
        child._dlt_parent_id as child_parent_dlt_id
    from parent
    inner join child
        on parent._dlt_id = child._dlt_parent_id
)

select *
from joined