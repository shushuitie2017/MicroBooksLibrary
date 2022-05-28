import React, {useState, useEffect} from 'react'
import axios from 'axios'
import { logRoles } from '@testing-library/react';
const ApiFetch = () => {

    const [posts, setPosts] = useState("");

    useEffect(() => {
        axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
        axios.get('http://localhost:8001')
        .then(res => {
            console.log(res)
            setPosts(res.data.title)
        })
    }, [])

    return (
        <div>
            { posts }
        </div>
    )
}

export default ApiFetch