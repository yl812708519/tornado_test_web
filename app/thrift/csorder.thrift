

const string WRITE_INFO = 'write_info'
const string WAIT_REVIEW = 'wait_review'
const string WAIT_DELEGATE = 'wait_delegate'
const string WAIT_PAYMENT = 'wait_payment'
const string PAID = 'paid'
const string COMPLETED = 'completed'
const string INVALID = 'invalid'
const string WAITE_UPLOAD = 'wait_upload'
const string STUFF_SEND = 'stuff_send'

exception Extest {

    1: i32 errorCode,
    2: string message,

}


service ThriftCSOrderService{
    string get_for_workbench(1:i64 csuser_id, 2: string order_id, 3: string treat_type, 4:i32 offset, 5:i32 count) throws (1: Extest se)
    i32 count_for_workbench(1: i64 csuser_id, 2: string order_id, 3: string treat_type) throws (1: Extest se)
    bool is_csuser_allowed(1: i64 csuser_id, 2: i64 order_id, 3: string treat_type) throws (1: Extest se)
    bool handle_csorder(1: i64 order_id, 2: string treat_type, 3: i64 stuff_id, 4: string next_status) throws (1: Extest se)
    string offline_payment(1: i64 order_id, 2: string order_type, 3: bool is_invoice, 4: string payment_json) throws (1: Extest se)
    //bool handle_cs_upload_order(1: i64 order_id, 2: string treat_type, 3: i64 stuff_id, 4: bool is_invalid)
}

service ThriftOrderStatusService{
    string gets_by_order_type(1: string order_type)
    bool update_order_status(1: i64 order_id, 2: string status, 3: i64 stuff_id)
    string get_order_status()
    string get_biz_status_by_type(1: string order_type, 2: bool is_paid_include)
    string get_dict_by_order_types(1: list<string> order_type)
    void reset_confirm(1: i64 stuff_id, 2: i64 order_id, 3: string order_type)
}

service ThriftOrderTipService{
    map<string, string> count_get_tips(1: i64 offset, 2 :i64 count)
}

service ThriftSmsNotifyService{
    string send_sms_notify(1: string mobile, 2: string temp_name, 3 :string args_json)
}

service ThriftCustomerRecordService{
    string gets_by_order_id(1: string order_id)
}
